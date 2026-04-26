from pathlib import Path
import os
import pandas as pd
from pymongo import MongoClient
from urllib.parse import quote_plus

project_root = Path(__file__).resolve().parents[2]
base = project_root / "Data" / "processed"
files = {
    "co2_country_year": base / "co2_country_year.csv",
    "happiness_country_year": base / "happiness_country_year.csv",
    "wdi_selected_long": base / "wdi_selected_long.csv",
    "country_year_master": base / "country_year_master.csv",
}

user = os.environ["MDB_APP_USER"]
pwd = quote_plus(os.environ["MDB_APP_PWD"])
uri = f"mongodb://{user}:{pwd}@127.0.0.1:27017/worlddb?authSource=worlddb"
db = MongoClient(uri)["worlddb"]

for coll, path in files.items():
    df = pd.read_csv(path)
    if "iso3" in df.columns:
        df["iso3"] = df["iso3"].astype(str).str.strip().str.upper()
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    docs = []
    for rec in df.to_dict("records"):
        clean = {}
        for k, v in rec.items():
            if pd.isna(v):
                clean[k] = None
            else:
                try:
                    clean[k] = v.item()
                except AttributeError:
                    clean[k] = v
        docs.append(clean)
    db[coll].delete_many({})
    for i in range(0, len(docs), 2000):
        db[coll].insert_many(docs[i:i+2000], ordered=False)
    print(coll, db[coll].count_documents({}))
