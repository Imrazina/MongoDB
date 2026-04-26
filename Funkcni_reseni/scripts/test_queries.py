#!/usr/bin/env python3
"""Run MongoDB query blocks from Dotazy markdown files.

Default use:
  ./scripts/test_queries.sh

The script reads ```javascript blocks from Dotazy/dotazy.md and executes each
block through mongosh inside the mongos container. It is meant as a quick
reproducibility check before defense/submission.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
COMPOSE_ROOT = SCRIPT_DIR.parent
PROJECT_ROOT = COMPOSE_ROOT.parent
DEFAULT_DOTAZY_FILE = PROJECT_ROOT / "Dotazy" / "dotazy.md"


@dataclass
class QueryBlock:
    number: int
    label: str
    code: str


def load_env(path: Path) -> dict[str, str]:
    env = os.environ.copy()
    if not path.exists():
        return env
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key] = value
    return env


def parse_query_blocks(markdown_path: Path) -> list[QueryBlock]:
    blocks: list[QueryBlock] = []
    current_category = "Bez kategorie"
    current_dotaz = "Bez cisla"
    in_code = False
    code_lines: list[str] = []

    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# Kategorie"):
            current_category = line.lstrip("# ").strip()
            continue
        if line.startswith("## Dotaz"):
            current_dotaz = line.lstrip("# ").strip()
            continue
        if line.strip() == "```javascript":
            in_code = True
            code_lines = []
            continue
        if in_code and line.strip() == "```":
            in_code = False
            label = f"{current_category} / {current_dotaz}"
            blocks.append(QueryBlock(len(blocks) + 1, label, "\n".join(code_lines).strip()))
            continue
        if in_code:
            code_lines.append(line)

    return blocks


def run_query(block: QueryBlock, env: dict[str, str], timeout: int) -> subprocess.CompletedProcess[str]:
    admin_user = env.get("MDB_ADMIN_USER")
    admin_pwd = env.get("MDB_ADMIN_PWD")
    if not admin_user or not admin_pwd:
        raise RuntimeError("Missing MDB_ADMIN_USER or MDB_ADMIN_PWD in .env")

    command = [
        "docker",
        "compose",
        "exec",
        "-T",
        "mongos",
        "mongosh",
        "--quiet",
        "--port",
        "27017",
        "-u",
        admin_user,
        "-p",
        admin_pwd,
        "--authenticationDatabase",
        "admin",
        "--eval",
        block.code + "\n;",
    ]
    return subprocess.run(
        command,
        cwd=COMPOSE_ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run MongoDB dotazy from markdown code blocks.")
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_DOTAZY_FILE,
        help=f"Markdown file with javascript blocks. Default: {DEFAULT_DOTAZY_FILE}",
    )
    parser.add_argument(
        "--only",
        type=int,
        help="Run only one query block by its sequential number from the markdown file.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Timeout per query in seconds. Default: 180.",
    )
    parser.add_argument(
        "--show-output",
        action="store_true",
        help="Print mongosh output for successful queries too.",
    )
    parser.add_argument(
        "--report",
        nargs="?",
        const=str(PROJECT_ROOT / "Dotazy" / "vystupy_dotazu.md"),
        help="Save outputs of all executed queries into a markdown report. Default path: Dotazy/vystupy_dotazu.md.",
    )
    parser.add_argument(
        "--stop-on-fail",
        action="store_true",
        help="Stop immediately after the first failed query.",
    )
    args = parser.parse_args()

    dotazy_file = args.file.resolve()
    if not dotazy_file.exists():
        print(f"[FAIL] Dotazy file does not exist: {dotazy_file}", file=sys.stderr)
        return 2

    env = load_env(COMPOSE_ROOT / ".env")
    blocks = parse_query_blocks(dotazy_file)
    if args.only is not None:
        blocks = [block for block in blocks if block.number == args.only]

    if not blocks:
        print(f"[FAIL] No javascript query blocks found in {dotazy_file}", file=sys.stderr)
        return 2

    print(f"Dotazy file: {dotazy_file}")
    print(f"Query blocks: {len(blocks)}")
    print("---")

    failed: list[tuple[QueryBlock, str]] = []
    report_sections: list[str] = []
    for block in blocks:
        print(f"[{block.number:02d}] {block.label} ... ", end="", flush=True)
        try:
            result = run_query(block, env, args.timeout)
        except subprocess.TimeoutExpired:
            message = f"timeout after {args.timeout}s"
            print(f"FAIL ({message})")
            failed.append((block, message))
            if args.stop_on_fail:
                break
            continue
        except Exception as exc:  # keep this practical for defense debugging
            message = str(exc)
            print(f"FAIL ({message})")
            failed.append((block, message))
            if args.stop_on_fail:
                break
            continue

        output = (result.stdout or "").strip()
        error = (result.stderr or "").strip()
        if result.returncode == 0:
            print("OK")
            if args.report is not None:
                report_output = output if output else "(bez vystupu)"
                report_sections.append(
                    f"## [{block.number:02d}] {block.label}\n\n"
                    "**Stav:** OK\n\n"
                    "```text\n"
                    f"{report_output}\n"
                    "```"
                )
            if args.show_output and output:
                print(output[:4000])
                if len(output) > 4000:
                    print("... output truncated by test_queries.py ...")
        else:
            message = error or output or f"mongosh exited with code {result.returncode}"
            print("FAIL")
            print(message[:4000])
            if args.report is not None:
                report_sections.append(
                    f"## [{block.number:02d}] {block.label}\n\n"
                    "**Stav:** FAIL\n\n"
                    "```text\n"
                    f"{message}\n"
                    "```"
                )
            failed.append((block, message))
            if args.stop_on_fail:
                break

    if args.report is not None:
        report_path = Path(args.report).expanduser()
        if not report_path.is_absolute():
            report_path = (Path.cwd() / report_path).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_text = (
            "# Vystupy Dotazu\n\n"
            f"Zdrojovy soubor dotazu: `{dotazy_file}`\n\n"
            f"Spusteno dotazu: `{len(blocks)}`\n\n"
            + "\n\n---\n\n".join(report_sections)
            + "\n"
        )
        report_path.write_text(report_text, encoding="utf-8")
        print(f"Report saved: {report_path}")

    print("---")
    if failed:
        print(f"FAILED: {len(failed)} / {len(blocks)}")
        for block, message in failed:
            first_line = message.splitlines()[0] if message else "unknown error"
            print(f"- [{block.number:02d}] {block.label}: {first_line}")
        return 1

    print(f"OK: {len(blocks)} / {len(blocks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
