from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Paths
# Skript je v: MongoDB/Funkcni_reseni/scripts
# Data jsou v: MongoDB/Data/processed
# ============================================================

BASE = Path(__file__).resolve().parents[2]   # MongoDB
DATA = BASE / "Data" / "processed"
OUT = DATA / "graphs"                       # MongoDB/Data/processed/graphs

OUT.mkdir(parents=True, exist_ok=True)


# ============================================================
# Load data
# ============================================================

master = pd.read_csv(DATA / "country_year_master.csv")
co2 = pd.read_csv(DATA / "co2_country_year.csv")
happy = pd.read_csv(DATA / "happiness_country_year.csv")
wdi = pd.read_csv(DATA / "wdi_selected_long.csv")


# ============================================================
# Basic cleaning
# ============================================================

def to_num(df: pd.DataFrame, cols: list[str]) -> None:
    for col in cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")


to_num(master, [
    "year",
    "happiness_score",
    "gdp_factor",
    "social_support_factor",
    "health_factor",
    "freedom_factor",
    "generosity_factor",
    "corruption_factor",
    "co2_total_mt",
    "co2_per_capita_t",
    "gdp_current_usd",
    "gdp_per_capita_usd",
    "internet_users_pct",
    "life_expectancy_years",
    "population_total",
    "trade_pct_gdp",
    "unemployment_pct",
    "urban_population_pct",
])

to_num(co2, [
    "year",
    "co2_total_mt",
    "co2_coal_mt",
    "co2_oil_mt",
    "co2_gas_mt",
    "co2_cement_mt",
    "co2_flaring_mt",
    "co2_other_mt",
    "co2_per_capita_t",
])

to_num(happy, [
    "year",
    "happiness_score",
    "gdp_factor",
    "social_support_factor",
    "health_factor",
    "freedom_factor",
    "generosity_factor",
    "corruption_factor",
])

to_num(wdi, [
    "year",
    "value",
])

for df in [master, co2, happy, wdi]:
    df["iso3"] = df["iso3"].astype(str).str.upper().str.strip()
    df["country"] = df["country"].astype(str).str.strip()


ANALYSIS_START = 2015
ANALYSIS_END = 2019


# ============================================================
# Helpers
# ============================================================

def save_plot(filename: str) -> None:
    plt.tight_layout()
    plt.savefig(OUT / filename, dpi=300, bbox_inches="tight")
    plt.close()


def add_linear_trend(x: pd.Series, y: pd.Series, log_x: bool = False) -> None:
    clean = pd.DataFrame({"x": x, "y": y}).dropna()
    clean = clean[clean["x"] > 0]

    if len(clean) < 2:
        return

    x_vals = np.log10(clean["x"]) if log_x else clean["x"]
    y_vals = clean["y"]

    coef = np.polyfit(x_vals, y_vals, 1)

    x_line_raw = np.linspace(clean["x"].min(), clean["x"].max(), 200)
    x_line_model = np.log10(x_line_raw) if log_x else x_line_raw
    y_line = coef[0] * x_line_model + coef[1]

    plt.plot(x_line_raw, y_line, linestyle="--", linewidth=2)


def year_span_label(series: pd.Series) -> str:
    vals = sorted(pd.Series(series).dropna().astype(int).unique())
    if not vals:
        return "bez dat"
    if len(vals) == 1:
        return str(vals[0])
    return f"{vals[0]}–{vals[-1]}"


def filter_master(required: list[str], extra=None) -> pd.DataFrame:
    df = master.dropna(subset=required).copy()
    df = df[(df["year"] >= ANALYSIS_START) & (df["year"] <= ANALYSIS_END)]
    if extra is not None:
        df = df[extra(df)]
    return df


# ============================================================
# 01 Trend happiness score by year (mean + median)
# ============================================================

df = filter_master(["year", "happiness_score"])
summary = (
    df.groupby("year", as_index=False)
    .agg(
        mean_happiness=("happiness_score", "mean"),
        median_happiness=("happiness_score", "median"),
        country_count=("iso3", "nunique"),
    )
    .sort_values("year")
)

plt.figure(figsize=(10, 5))
plt.plot(summary["year"], summary["mean_happiness"], marker="o", linewidth=2, label="Průměr")
plt.plot(summary["year"], summary["median_happiness"], marker="s", linewidth=2, label="Medián")

for _, row in summary.iterrows():
    plt.text(row["year"], row["mean_happiness"] + 0.015, f"n={int(row['country_count'])}", ha="center", fontsize=8)

plt.title("Vývoj happiness score podle roku")
plt.xlabel("Rok")
plt.ylabel("Happiness score")
plt.xticks(summary["year"])
plt.legend()
plt.grid(alpha=0.3)

save_plot("01_line_happiness_by_year.png")


# ============================================================
# 02 Happiness residual relative to GDP trend
# ============================================================

df = filter_master(
    ["country", "iso3", "year", "gdp_per_capita_usd", "happiness_score"],
    extra=lambda d: d["gdp_per_capita_usd"] > 0,
)

df["log_gdp"] = np.log10(df["gdp_per_capita_usd"])
coef = np.polyfit(df["log_gdp"], df["happiness_score"], 1)
df["predicted_happiness"] = coef[0] * df["log_gdp"] + coef[1]
df["happiness_residual"] = df["happiness_score"] - df["predicted_happiness"]

resid = (
    df.groupby(["iso3", "country"], as_index=False)
    .agg(
        avg_residual=("happiness_residual", "mean"),
        years_observed=("year", "count"),
    )
)
resid = resid[resid["years_observed"] >= 3]
resid_top = pd.concat([
    resid.sort_values("avg_residual", ascending=False).head(8),
    resid.sort_values("avg_residual", ascending=True).head(8),
], ignore_index=True)
resid_top = resid_top.drop_duplicates(subset=["iso3"]).sort_values("avg_residual")
colors = ["#c44e52" if x < 0 else "#4c72b0" for x in resid_top["avg_residual"]]

plt.figure(figsize=(11, 7))
plt.barh(resid_top["country"], resid_top["avg_residual"], color=colors)
plt.axvline(0, color="black", linewidth=1)
plt.title(f"Země nad a pod očekávanou úrovní happiness vzhledem k GDP ({year_span_label(df['year'])})")
plt.xlabel("Průměrné residuum happiness score vůči trendu GDP")
plt.ylabel("Země")
plt.grid(axis="x", alpha=0.3)

save_plot("02_bar_happiness_residual_vs_gdp.png")


# ============================================================
# 03 Scatter GDP per capita vs happiness score + trend line
# ============================================================

df = filter_master(
    ["gdp_per_capita_usd", "happiness_score"],
    extra=lambda d: d["gdp_per_capita_usd"] > 0,
)

corr = np.log10(df["gdp_per_capita_usd"]).corr(df["happiness_score"])
span = year_span_label(df["year"])

plt.figure(figsize=(10, 6))
plt.scatter(df["gdp_per_capita_usd"], df["happiness_score"], alpha=0.65)
add_linear_trend(df["gdp_per_capita_usd"], df["happiness_score"], log_x=True)
plt.xscale("log")
plt.title(f"Vztah mezi GDP per capita a happiness score ({span}), korelace log(GDP): {corr:.2f}")
plt.xlabel("GDP per capita (USD, log osa)")
plt.ylabel("Happiness score")
plt.grid(alpha=0.3)

save_plot("03_scatter_gdp_happiness_trend.png")


# ============================================================
# 04 Scatter CO2 per capita vs happiness score by GDP bucket
# ============================================================

df = filter_master(
    ["co2_per_capita_t", "happiness_score", "gdp_per_capita_usd"],
    extra=lambda d: (d["co2_per_capita_t"] > 0) & (d["gdp_per_capita_usd"] > 0),
)

bins = [0, 5000, 10000, 20000, 40000, 80000, np.inf]
labels = ["< 5k", "5k–10k", "10k–20k", "20k–40k", "40k–80k", "80k+"]

df["gdp_bucket"] = pd.cut(
    df["gdp_per_capita_usd"],
    bins=bins,
    labels=labels,
    include_lowest=True,
)

plt.figure(figsize=(11, 7))
for bucket in labels:
    part = df[df["gdp_bucket"] == bucket]
    if len(part) == 0:
        continue
    plt.scatter(part["co2_per_capita_t"], part["happiness_score"], alpha=0.65, label=bucket)

plt.xscale("log")
plt.title(f"Vztah mezi CO2 per capita a happiness score podle GDP skupin ({year_span_label(df['year'])})")
plt.xlabel("CO2 per capita (t, log osa)")
plt.ylabel("Happiness score")
plt.legend(title="GDP per capita")
plt.grid(alpha=0.3)

save_plot("04_scatter_co2_happiness_by_gdp_bucket.png")


# ============================================================
# 05 Bubble chart: GDP, happiness, population, CO2
# ============================================================

df = filter_master(
    ["gdp_per_capita_usd", "happiness_score", "population_total", "co2_per_capita_t"],
    extra=lambda d: (d["gdp_per_capita_usd"] > 0) & (d["population_total"] > 0) & (d["co2_per_capita_t"] > 0),
)

sizes = np.sqrt(df["population_total"]) / 250

plt.figure(figsize=(11, 7))
scatter = plt.scatter(
    df["gdp_per_capita_usd"],
    df["happiness_score"],
    s=sizes,
    c=df["co2_per_capita_t"],
    alpha=0.65,
)
plt.xscale("log")
plt.colorbar(scatter, label="CO2 per capita (t)")
plt.title(f"GDP, happiness, populace a CO2 per capita ({year_span_label(df['year'])})")
plt.xlabel("GDP per capita (USD, log osa)")
plt.ylabel("Happiness score")
plt.grid(alpha=0.3)

save_plot("05_bubble_gdp_happiness_population_co2.png")


# ============================================================
# 06 Quadrant chart: happiness vs CO2
# ============================================================

df = filter_master(
    ["happiness_score", "co2_per_capita_t", "gdp_per_capita_usd"],
    extra=lambda d: (d["co2_per_capita_t"] > 0) & (d["gdp_per_capita_usd"] > 0),
)

happiness_median = df["happiness_score"].median()
co2_median = df["co2_per_capita_t"].median()


def quadrant(row: pd.Series) -> str:
    if row["happiness_score"] >= happiness_median and row["co2_per_capita_t"] < co2_median:
        return "Vysoké štěstí / nízké CO2"
    if row["happiness_score"] >= happiness_median and row["co2_per_capita_t"] >= co2_median:
        return "Vysoké štěstí / vysoké CO2"
    if row["happiness_score"] < happiness_median and row["co2_per_capita_t"] < co2_median:
        return "Nízké štěstí / nízké CO2"
    return "Nízké štěstí / vysoké CO2"


df["quadrant"] = df.apply(quadrant, axis=1)

plt.figure(figsize=(11, 7))
for q in [
    "Vysoké štěstí / nízké CO2",
    "Vysoké štěstí / vysoké CO2",
    "Nízké štěstí / nízké CO2",
    "Nízké štěstí / vysoké CO2",
]:
    part = df[df["quadrant"] == q]
    if len(part) == 0:
        continue
    plt.scatter(part["co2_per_capita_t"], part["happiness_score"], alpha=0.65, label=q)

plt.axhline(happiness_median, linestyle="--", linewidth=1)
plt.axvline(co2_median, linestyle="--", linewidth=1)
plt.xscale("log")
plt.title(f"Rozdělení zemí podle happiness score a CO2 per capita ({year_span_label(df['year'])})")
plt.xlabel("CO2 per capita (t, log osa)")
plt.ylabel("Happiness score")
plt.legend()
plt.grid(alpha=0.3)

save_plot("06_quadrant_happiness_co2.png")


# ============================================================
# 07 Wellbeing efficiency ranking
# ============================================================

df = filter_master(
    ["country", "year", "happiness_score", "co2_per_capita_t", "gdp_per_capita_usd"],
    extra=lambda d: (d["co2_per_capita_t"] > 0) & (d["gdp_per_capita_usd"] >= 15000),
)

df["wellbeing_efficiency"] = df["happiness_score"] / df["co2_per_capita_t"]

eff = (
    df.groupby(["iso3", "country"], as_index=False)
    .agg(
        avg_happiness=("happiness_score", "mean"),
        avg_co2_per_capita=("co2_per_capita_t", "mean"),
        avg_gdp_per_capita=("gdp_per_capita_usd", "mean"),
        wellbeing_efficiency=("wellbeing_efficiency", "mean"),
        years_observed=("year", "count"),
    )
)

eff = eff[eff["years_observed"] >= 3]
eff_top = eff.sort_values("wellbeing_efficiency", ascending=False).head(15)
eff_top = eff_top.sort_values("wellbeing_efficiency")

plt.figure(figsize=(10, 7))
plt.barh(eff_top["country"], eff_top["wellbeing_efficiency"])
plt.title(f"Top země podle wellbeing efficiency ({year_span_label(df['year'])})")
plt.xlabel("Happiness score / CO2 per capita")
plt.ylabel("Země")
plt.grid(axis="x", alpha=0.3)

save_plot("07_bar_wellbeing_efficiency.png")


# ============================================================
# 08 Change in happiness vs change in CO2 per capita
# ============================================================

df = filter_master(
    ["iso3", "country", "year", "happiness_score", "co2_per_capita_t"],
    extra=lambda d: d["co2_per_capita_t"] > 0,
)
df = df.sort_values(["iso3", "year"])

rows = []
for iso3, group in df.groupby("iso3"):
    group = group.sort_values("year")
    if group["year"].nunique() < 3:
        continue

    first = group.iloc[0]
    last = group.iloc[-1]
    if last["year"] <= first["year"] or first["co2_per_capita_t"] <= 0:
        continue

    happiness_delta = last["happiness_score"] - first["happiness_score"]
    co2_change_pct = ((last["co2_per_capita_t"] - first["co2_per_capita_t"]) / first["co2_per_capita_t"]) * 100

    rows.append({
        "iso3": iso3,
        "country": last["country"],
        "first_year": int(first["year"]),
        "last_year": int(last["year"]),
        "happiness_delta": happiness_delta,
        "co2_change_pct": co2_change_pct,
    })

changes = pd.DataFrame(rows)
changes["pattern"] = np.where(
    (changes["happiness_delta"] >= 0) & (changes["co2_change_pct"] < 0),
    "Vyšší happiness / nižší CO2",
    np.where(
        (changes["happiness_delta"] >= 0) & (changes["co2_change_pct"] >= 0),
        "Vyšší happiness / vyšší CO2",
        np.where(
            (changes["happiness_delta"] < 0) & (changes["co2_change_pct"] < 0),
            "Nižší happiness / nižší CO2",
            "Nižší happiness / vyšší CO2",
        ),
    ),
)

plt.figure(figsize=(11, 7))
for label, part in changes.groupby("pattern"):
    plt.scatter(part["co2_change_pct"], part["happiness_delta"], alpha=0.7, label=label)

for _, row in changes.assign(score=changes["happiness_delta"].abs() + changes["co2_change_pct"].abs() / 50).nlargest(8, "score").iterrows():
    plt.text(row["co2_change_pct"], row["happiness_delta"], row["iso3"], fontsize=8)

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.title(f"Změna happiness score a CO2 per capita mezi roky {int(changes['first_year'].min())}–{int(changes['last_year'].max())}")
plt.xlabel("Změna CO2 per capita (%)")
plt.ylabel("Změna happiness score")
plt.legend()
plt.grid(alpha=0.3)

save_plot("08_scatter_change_happiness_vs_co2.png")


# ============================================================
# 09 Average rank gap by country
# ============================================================

df = filter_master(
    ["year", "country", "happiness_score", "co2_per_capita_t"],
    extra=lambda d: d["co2_per_capita_t"] > 0,
)

df["happiness_rank"] = df.groupby("year")["happiness_score"].rank(ascending=False, method="min")
df["low_co2_rank"] = df.groupby("year")["co2_per_capita_t"].rank(ascending=True, method="min")
df["rank_gap"] = df["low_co2_rank"] - df["happiness_rank"]

rank_avg = (
    df.groupby(["iso3", "country"], as_index=False)
    .agg(
        avg_rank_gap=("rank_gap", "mean"),
        years_observed=("year", "count"),
    )
)
rank_avg = rank_avg[rank_avg["years_observed"] >= 3]
rank_top = rank_avg.assign(abs_rank_gap=rank_avg["avg_rank_gap"].abs())
rank_top = rank_top.sort_values("abs_rank_gap", ascending=False).head(15)
rank_top = rank_top.sort_values("avg_rank_gap")

plt.figure(figsize=(11, 7))
plt.barh(rank_top["country"], rank_top["avg_rank_gap"])
plt.axvline(0, linewidth=1)
plt.title("Průměrný rozdíl mezi pořadím podle happiness a nízkého CO2")
plt.xlabel("Průměrný rank gap: low CO2 rank - happiness rank")
plt.ylabel("Země")
plt.grid(axis="x", alpha=0.3)

save_plot("09_bar_rank_gap_happiness_low_co2.png")


# ============================================================
# 10 Trajectory chart for selected countries
# ============================================================

selected_iso3 = ["CZE", "FIN", "USA", "IND", "CHN", "DEU"]

df = filter_master(
    ["iso3", "country", "year", "happiness_score", "co2_per_capita_t"],
    extra=lambda d: (d["co2_per_capita_t"] > 0) & (d["iso3"].isin(selected_iso3)),
)

plt.figure(figsize=(11, 7))
for iso3, group in df.groupby("iso3"):
    group = group.sort_values("year")
    label = group["country"].iloc[0]

    plt.plot(group["co2_per_capita_t"], group["happiness_score"], marker="o", linewidth=2, label=label)

    first = group.iloc[0]
    last = group.iloc[-1]
    plt.text(first["co2_per_capita_t"], first["happiness_score"], str(int(first["year"])), fontsize=8, ha="right")
    plt.text(last["co2_per_capita_t"], last["happiness_score"], str(int(last["year"])), fontsize=8, ha="left")

plt.xscale("log")
plt.title("Vývoj vybraných zemí: CO2 per capita a happiness score")
plt.xlabel("CO2 per capita (t, log osa)")
plt.ylabel("Happiness score")
plt.legend()
plt.grid(alpha=0.3)

save_plot("10_trajectory_selected_countries.png")


# ============================================================
# 11 CO2 composition for top countries in selected year
# ============================================================

selected_year = 2019

df = co2.dropna(subset=[
    "year",
    "country",
    "co2_total_mt",
    "co2_coal_mt",
    "co2_oil_mt",
    "co2_gas_mt",
    "co2_cement_mt",
    "co2_flaring_mt",
    "co2_other_mt",
]).copy()

df = df[df["year"] == selected_year]
df = df[df["co2_total_mt"] > 0]
df = df[~df["country"].isin(["Global", "World"])]

top = df.sort_values("co2_total_mt", ascending=False).head(10).copy()

components = [
    "co2_coal_mt",
    "co2_oil_mt",
    "co2_gas_mt",
    "co2_cement_mt",
    "co2_flaring_mt",
    "co2_other_mt",
]
labels = ["Coal", "Oil", "Gas", "Cement", "Flaring", "Other"]

top = top.sort_values("co2_total_mt")

plt.figure(figsize=(11, 7))
left = np.zeros(len(top))
for col, label in zip(components, labels):
    values = top[col].fillna(0).to_numpy()
    plt.barh(top["country"], values, left=left, label=label)
    left += values

plt.title(f"Složení emisí CO2 podle zdroje, top 10 zemí v roce {selected_year}")
plt.xlabel("CO2 emise (Mt)")
plt.ylabel("Země")
plt.legend()
plt.grid(axis="x", alpha=0.3)

save_plot("11_stacked_co2_composition_top10.png")


# ============================================================
# 12 WDI indicator availability
# ============================================================

df = wdi.dropna(subset=["indicator", "value"]).copy()

availability = (
    df.groupby("indicator", as_index=False)
    .agg(
        records=("value", "count"),
        countries=("iso3", "nunique"),
        first_year=("year", "min"),
        last_year=("year", "max"),
    )
    .sort_values("records", ascending=True)
)

plt.figure(figsize=(10, 6))
plt.barh(availability["indicator"], availability["records"])
plt.title("Dostupnost vybraných WDI indikátorů")
plt.xlabel("Počet dostupných hodnot")
plt.ylabel("Indikátor")
plt.grid(axis="x", alpha=0.3)

save_plot("12_bar_wdi_indicator_availability.png")

print(f"Hotovo. Grafy byly uloženy do složky: {OUT}")
