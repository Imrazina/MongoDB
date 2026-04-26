#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
set -a
# shellcheck disable=SC1090
source "$COMPOSE_ROOT/.env"
set +a
cd "$COMPOSE_ROOT"
docker compose exec mongos mongosh --port 27017 -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" --authenticationDatabase admin --eval '
db = db.getSiblingDB("worlddb");
print("co2:", db.co2_country_year.countDocuments());
print("happy:", db.happiness_country_year.countDocuments());
print("wdi:", db.wdi_selected_long.countDocuments());
print("master:", db.country_year_master.countDocuments());
sh.status();
'
