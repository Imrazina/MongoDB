#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ ! -f "$COMPOSE_ROOT/.env" ]; then
  cp "$COMPOSE_ROOT/.env.example" "$COMPOSE_ROOT/.env"
fi

cd "$COMPOSE_ROOT"

docker compose down -v --remove-orphans
docker compose up -d

wait_service_exit_ok() {
  local service="$1"
  local timeout_seconds="${2:-600}"
  local waited=0

  while [ "$waited" -lt "$timeout_seconds" ]; do
    local cid
    cid="$(docker compose ps -q "$service")"
    if [ -n "$cid" ]; then
      local status
      status="$(docker inspect -f '{{.State.Status}}' "$cid")"
      if [ "$status" = "exited" ]; then
        local exit_code
        exit_code="$(docker inspect -f '{{.State.ExitCode}}' "$cid")"
        if [ "$exit_code" -ne 0 ]; then
          echo "Service '$service' failed with exit code $exit_code" >&2
          docker compose logs "$service" >&2 || true
          exit 1
        fi
        echo "Service '$service' completed successfully"
        return 0
      fi
    fi
    sleep 2
    waited=$((waited + 2))
  done

  echo "Timeout waiting for service '$service' to complete" >&2
  docker compose logs "$service" >&2 || true
  exit 1
}

wait_service_exit_ok initializer 600
wait_service_exit_ok data-loader 1200

"$SCRIPT_DIR/check_cluster.sh"
