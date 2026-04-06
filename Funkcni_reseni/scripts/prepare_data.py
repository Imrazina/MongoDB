from pathlib import Path
import pandas as pd
import country_converter as coco

base = Path.home() / "BSQBD_ShabossovaAnna"
raw = base / "Data" / "raw"
processed = base / "Data" / "processed"
processed.mkdir(parents=True, exist_ok=True)

def pick_one(pattern: str) -> Path:
    matches = sorted(raw.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"Not found: {pattern}")
    return matches[0]

# ---------- CO2 ----------
co2_path = pick_one("co2/**/GCB2022v27_MtCO2_flat.csv")
co2 = pd.read_csv(co2_path)
co2 = co2.rename(columns={
    "Country": "country",
    "ISO 3166-1 alpha-3": "iso3",
    "Year": "year",
    "Total": "co2_total_mt",
    "Per Capita": "co2_per_capita_t",
    "Coal": "co2_coal_mt",
    "Oil": "co2_oil_mt",
    "Gas": "co2_gas_mt",
    "Cement": "co2_cement_mt",
    "Flaring": "co2_flaring_mt",
    "Other": "co2_other_mt",
})
co2["year"] = pd.to_numeric(co2["year"], errors="coerce").astype("Int64")
co2 = co2[co2["iso3"].notna() & (co2["iso3"].str.len() == 3)]
co2.to_csv(processed / "co2_country_year.csv", index=False)

# ---------- Happiness ----------
happiness_dir = raw / "world_happiness"
h_files = sorted(happiness_dir.glob("*.csv"))
if not h_files:
    raise FileNotFoundError("No CSV files in world_happiness")

def find_col(cols, checks):
    for c in cols:
        l = c.lower().replace(".", " ").replace("_", " ").strip()
        if any(chk in l for chk in checks):
            return c
    return None

parts = []
for fp in h_files:
    year = int(fp.stem)
    df = pd.read_csv(fp)

    country_col = find_col(df.columns, ["country"])
    score_col = None
    for cand in ["Happiness Score", "Happiness.Score", "Score"]:
        if cand in df.columns:
            score_col = cand
            break
    if not score_col:
        score_col = find_col(df.columns, ["happiness score", "score"])

    gdp_col = find_col(df.columns, ["gdp", "economy"])
    social_col = find_col(df.columns, ["social support", "family"])
    life_col = find_col(df.columns, ["health", "life expectancy"])
    freedom_col = find_col(df.columns, ["freedom"])
    generosity_col = find_col(df.columns, ["generosity"])
    corruption_col = find_col(df.columns, ["corruption", "trust"])

    out = pd.DataFrame({
        "country": df[country_col] if country_col else None,
        "year": year,
        "happiness_score": df[score_col] if score_col else None,
        "gdp_factor": df[gdp_col] if gdp_col else None,
        "social_support_factor": df[social_col] if social_col else None,
        "health_factor": df[life_col] if life_col else None,
        "freedom_factor": df[freedom_col] if freedom_col else None,
        "generosity_factor": df[generosity_col] if generosity_col else None,
        "corruption_factor": df[corruption_col] if corruption_col else None,
    })
    parts.append(out)

happy = pd.concat(parts, ignore_index=True)
happy["iso3"] = coco.convert(names=happy["country"], to="ISO3")

manual_iso = {
    "Congo (Brazzaville)": "COG",
    "Congo (Kinshasa)": "COD",
    "Czech Republic": "CZE",
    "Hong Kong S.A.R., China": "HKG",
    "Ivory Coast": "CIV",
    "Kosovo": "XKX",
    "North Cyprus": "CYP",
    "South Korea": "KOR",
    "Taiwan Province of China": "TWN",
    "Trinidad & Tobago": "TTO",
}
happy["iso3"] = happy.apply(lambda r: manual_iso.get(str(r["country"]), r["iso3"]), axis=1)
happy = happy[happy["iso3"].notna() & (happy["iso3"] != "not found")]
happy["year"] = pd.to_numeric(happy["year"], errors="coerce").astype("Int64")
happy.to_csv(processed / "happiness_country_year.csv", index=False)

# ---------- WDI ----------
wdi_path = pick_one("wdi/**/WDIData.csv")
wdi = pd.read_csv(wdi_path, low_memory=False)
indicators = {
    "NY.GDP.PCAP.CD": "gdp_per_capita_usd",
    "NY.GDP.MKTP.CD": "gdp_current_usd",
    "SP.POP.TOTL": "population_total",
    "SP.DYN.LE00.IN": "life_expectancy_years",
    "SL.UEM.TOTL.ZS": "unemployment_pct",
    "SP.URB.TOTL.IN.ZS": "urban_population_pct",
    "NE.TRD.GNFS.ZS": "trade_pct_gdp",
    "IT.NET.USER.ZS": "internet_users_pct",
}
year_cols = [c for c in wdi.columns if c.isdigit()]
wdi_sel = wdi[wdi["Indicator Code"].isin(indicators.keys())].copy()

wdi_long = wdi_sel[["Country Name", "Country Code", "Indicator Code"] + year_cols].melt(
    id_vars=["Country Name", "Country Code", "Indicator Code"],
    var_name="year",
    value_name="value",
)
wdi_long = wdi_long.rename(columns={
    "Country Name": "country",
    "Country Code": "iso3",
    "Indicator Code": "indicator_code",
})
wdi_long["year"] = pd.to_numeric(wdi_long["year"], errors="coerce").astype("Int64")
wdi_long["value"] = pd.to_numeric(wdi_long["value"], errors="coerce")
wdi_long = wdi_long.dropna(subset=["value"])
wdi_long["indicator"] = wdi_long["indicator_code"].map(indicators)
wdi_long.to_csv(processed / "wdi_selected_long.csv", index=False)

wdi_wide = wdi_long.pivot_table(
    index=["iso3", "country", "year"],
    columns="indicator",
    values="value",
    aggfunc="first",
).reset_index()
wdi_wide.to_csv(processed / "wdi_selected_country_year.csv", index=False)

# ---------- Master join ----------
master = happy.merge(
    co2[["iso3", "year", "co2_total_mt", "co2_per_capita_t"]],
    on=["iso3", "year"],
    how="left",
).merge(
    wdi_wide.drop(columns=["country"], errors="ignore"),
    on=["iso3", "year"],
    how="left",
)
master.to_csv(processed / "country_year_master.csv", index=False)

print("DONE")
for fn in [
    "co2_country_year.csv",
    "happiness_country_year.csv",
    "wdi_selected_long.csv",
    "wdi_selected_country_year.csv",
    "country_year_master.csv",
]:
    p = processed / fn
    print(f"{fn}: {sum(1 for _ in open(p, 'r', encoding='utf-8')) - 1} rows")
