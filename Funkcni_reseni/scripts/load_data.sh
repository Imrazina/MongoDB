#!/usr/bin/env bash
set -euo pipefail

: "${MDB_ADMIN_USER:?MDB_ADMIN_USER is required}"
: "${MDB_ADMIN_PWD:?MDB_ADMIN_PWD is required}"
: "${MDB_APP_USER:?MDB_APP_USER is required}"
: "${MDB_APP_PWD:?MDB_APP_PWD is required}"

wait_auth_mongos() {
  local attempt
  for attempt in $(seq 1 120); do
    if mongosh --host mongos --port 27017 -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" --authenticationDatabase admin --quiet --eval 'quit(db.adminCommand({ ping: 1 }).ok === 1 ? 0 : 1)' >/dev/null 2>&1; then
      echo "[loader] mongos auth is ready"
      return 0
    fi
    sleep 2
  done
  echo "[loader] timeout waiting for mongos auth" >&2
  exit 1
}

import_csv() {
  local collection="$1"
  local file_name="$2"
  local typed_header="$3"
  local tmp_file="/tmp/${collection}_typed.csv"

  {
    echo "$typed_header"
    tail -n +2 "/dataset/$file_name"
  } > "$tmp_file"

  mongoimport \
    --host mongos \
    --port 27017 \
    -u "$MDB_APP_USER" \
    -p "$MDB_APP_PWD" \
    --authenticationDatabase worlddb \
    --db worlddb \
    --collection "$collection" \
    --type csv \
    --headerline \
    --columnsHaveTypes \
    --ignoreBlanks \
    --file "$tmp_file"
}

wait_auth_mongos

mongosh --host mongos --port 27017 -u "$MDB_APP_USER" -p "$MDB_APP_PWD" --authenticationDatabase worlddb --quiet --eval '
db = db.getSiblingDB("worlddb");
db.co2_country_year.deleteMany({});
db.happiness_country_year.deleteMany({});
db.wdi_selected_long.deleteMany({});
db.country_year_master.deleteMany({});
'

import_csv "co2_country_year" "co2_country_year.csv" "country.string(),iso3.string(),year.int32(),co2_total_mt.double(),co2_coal_mt.double(),co2_oil_mt.double(),co2_gas_mt.double(),co2_cement_mt.double(),co2_flaring_mt.double(),co2_other_mt.double(),co2_per_capita_t.double()"
import_csv "happiness_country_year" "happiness_country_year.csv" "country.string(),year.int32(),happiness_score.double(),gdp_factor.double(),social_support_factor.double(),health_factor.double(),freedom_factor.double(),generosity_factor.double(),corruption_factor.double(),iso3.string()"
import_csv "wdi_selected_long" "wdi_selected_long.csv" "country.string(),iso3.string(),indicator_code.string(),year.int32(),value.double(),indicator.string()"
import_csv "country_year_master" "country_year_master.csv" "country.string(),year.int32(),happiness_score.double(),gdp_factor.double(),social_support_factor.double(),health_factor.double(),freedom_factor.double(),generosity_factor.double(),corruption_factor.double(),iso3.string(),co2_total_mt.double(),co2_per_capita_t.double(),gdp_current_usd.double(),gdp_per_capita_usd.double(),internet_users_pct.double(),life_expectancy_years.double(),population_total.double(),trade_pct_gdp.double(),unemployment_pct.double(),urban_population_pct.double()"

mongosh --host mongos --port 27017 -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" --authenticationDatabase admin --quiet --eval '
db = db.getSiblingDB("worlddb");

try { sh.splitAt("worlddb.co2_country_year", { iso3: "GRC", year: 1754 }); } catch (e) { print(e.message); }
try { sh.splitAt("worlddb.co2_country_year", { iso3: "MDG", year: 1974 }); } catch (e) { print(e.message); }
try { sh.moveChunk("worlddb.co2_country_year", { iso3: "AFG", year: 1900 }, "shard3RS"); } catch (e) { print(e.message); }
try { sh.moveChunk("worlddb.co2_country_year", { iso3: "KWT", year: 1900 }, "shard2RS"); } catch (e) { print(e.message); }

try { sh.splitAt("worlddb.wdi_selected_long", { iso3: "HUN", year: 1994, indicator: "gdp_current_usd" }); } catch (e) { print(e.message); }
try { sh.splitAt("worlddb.wdi_selected_long", { iso3: "MMR", year: 1985, indicator: "life_expectancy_years" }); } catch (e) { print(e.message); }
try { sh.moveChunk("worlddb.wdi_selected_long", { iso3: "BIH", year: 2006, indicator: "gdp_per_capita_usd" }, "shard3RS"); } catch (e) { print(e.message); }
try { sh.moveChunk("worlddb.wdi_selected_long", { iso3: "NGA", year: 2000, indicator: "gdp_per_capita_usd" }, "shard2RS"); } catch (e) { print(e.message); }

print("co2_country_year", db.co2_country_year.countDocuments());
print("happiness_country_year", db.happiness_country_year.countDocuments());
print("wdi_selected_long", db.wdi_selected_long.countDocuments());
print("country_year_master", db.country_year_master.countDocuments());
'

echo "[loader] import and chunk distribution complete"
