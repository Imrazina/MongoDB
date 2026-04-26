from pathlib import Path

import pandas as pd


BASE = Path(__file__).resolve().parent
PROCESSED = BASE / "processed"
SUMMARY_FILE = PROCESSED / "data_quality_summary.csv"
STATS_FILE = PROCESSED / "basic_statistics_summary.csv"

FILES = [
    "co2_country_year.csv",
    "happiness_country_year.csv",
    "wdi_selected_long.csv",
    "wdi_selected_country_year.csv",
    "country_year_master.csv",
]

# Metrics used in the documentation tables. They cover subjective wellbeing,
# emissions, economic level and selected social indicators.
STAT_METRICS = [
    ("happiness_country_year.csv", "happiness_score"),
    ("co2_country_year.csv", "co2_per_capita_t"),
    ("co2_country_year.csv", "co2_total_mt"),
    ("country_year_master.csv", "gdp_per_capita_usd"),
    ("country_year_master.csv", "life_expectancy_years"),
    ("country_year_master.csv", "internet_users_pct"),
]


def safe_min(df: pd.DataFrame, column: str):
    if column not in df.columns:
        return None
    values = pd.to_numeric(df[column], errors="coerce").dropna()
    return int(values.min()) if not values.empty else None


def safe_max(df: pd.DataFrame, column: str):
    if column not in df.columns:
        return None
    values = pd.to_numeric(df[column], errors="coerce").dropna()
    return int(values.max()) if not values.empty else None


def load_processed_csv(file_name: str) -> pd.DataFrame:
    path = PROCESSED / file_name
    if not path.exists():
        raise FileNotFoundError(f"Missing processed dataset: {path}")
    return pd.read_csv(path)


def analyze_file(file_name: str) -> dict:
    df = load_processed_csv(file_name)
    numeric_cols = df.select_dtypes(include="number").columns

    row = {
        "file": file_name,
        "rows": len(df),
        "columns": len(df.columns),
        "numeric_columns": len(numeric_cols),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "year_min": safe_min(df, "year"),
        "year_max": safe_max(df, "year"),
        "country_count": int(df["iso3"].nunique()) if "iso3" in df.columns else None,
    }

    print("=" * 80)
    print(file_name)
    print(f"Rows: {row['rows']}")
    print(f"Columns: {row['columns']}")
    print(f"Numeric columns: {row['numeric_columns']}")
    print(f"Missing cells: {row['missing_cells']}")
    print(f"Duplicate rows: {row['duplicate_rows']}")
    print(f"Year range: {row['year_min']} - {row['year_max']}")
    print(f"Country count: {row['country_count']}")

    print("\nMissing values by column:")
    print(df.isna().sum().to_string())

    print("\nNumeric statistics:")
    print(df.describe(include="number").to_string())

    return row


def analyze_metric(file_name: str, column: str) -> dict:
    df = load_processed_csv(file_name)
    if column not in df.columns:
        raise KeyError(f"Column {column!r} is missing in {file_name}")

    values = pd.to_numeric(df[column], errors="coerce").dropna()
    if values.empty:
        raise ValueError(f"Column {column!r} in {file_name} has no numeric values")

    return {
        "metric": column,
        "file": file_name,
        "count": int(values.count()),
        "min": float(values.min()),
        "max": float(values.max()),
        "mean": float(values.mean()),
        "median": float(values.median()),
        "sum": float(values.sum()),
    }


def main() -> None:
    if not PROCESSED.exists():
        raise FileNotFoundError(f"Processed data directory does not exist: {PROCESSED}")

    summary = pd.DataFrame(analyze_file(file_name) for file_name in FILES)
    summary.to_csv(SUMMARY_FILE, index=False)

    statistics = pd.DataFrame(
        analyze_metric(file_name, column) for file_name, column in STAT_METRICS
    )
    statistics.to_csv(STATS_FILE, index=False)

    print("=" * 80)
    print(f"Summary saved to: {SUMMARY_FILE}")
    print(f"Basic statistics saved to: {STATS_FILE}")


if __name__ == "__main__":
    main()
