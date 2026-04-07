#!/usr/bin/env bash
set -euo pipefail

NODE="${1:-sh1a}"

cd ~/BSQBD_ShabossovaAnna/Funkcni_reseni
source ~/.bsqbd_world_env

echo "== BEFORE =="
docker compose ps "$NODE"

echo "== STOP NODE: $NODE =="
docker compose stop "$NODE"

sleep 5

echo "== QUERY THROUGH MONGOS AFTER NODE FAILURE =="
docker compose exec mongos mongosh --port 27017 \
  -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" \
  --authenticationDatabase admin --eval '
db=db.getSiblingDB("worlddb");
print("co2", db.co2_country_year.countDocuments());
print("happy", db.happiness_country_year.countDocuments());
print("wdi", db.wdi_selected_long.countDocuments());
print("master", db.country_year_master.countDocuments());
'

echo "== START NODE: $NODE =="
docker compose start "$NODE"

sleep 5

echo "== AFTER RECOVERY =="
docker compose ps "$NODE"
