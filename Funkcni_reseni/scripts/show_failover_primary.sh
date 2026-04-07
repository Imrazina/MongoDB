#!/usr/bin/env bash
set -euo pipefail

SHARD="${1:-sh1}"
NODES=("${SHARD}a" "${SHARD}b" "${SHARD}c")

cd ~/BSQBD_ShabossovaAnna/Funkcni_reseni
source ~/.bsqbd_world_env

role_of() {
  local node="$1"
  docker compose exec -T "$node" mongosh --quiet --port 27018 --eval '
    const h = db.hello();
    if (h.isWritablePrimary) print("PRIMARY");
    else if (h.secondary) print("SECONDARY");
    else print("OTHER");
  ' 2>/dev/null || echo "DOWN"
}

primary_host_of() {
  local node="$1"
  docker compose exec -T "$node" mongosh --quiet --port 27018 --eval '
    const h = db.hello();
    print(h.primary || "");
  ' 2>/dev/null || true
}

print_roles() {
  for node in "${NODES[@]}"; do
    printf "%s: %s\n" "$node" "$(role_of "$node")"
  done
}

find_primary_service() {
  for node in "${NODES[@]}"; do
    if [ "$(role_of "$node")" = "PRIMARY" ]; then
      echo "$node"
      return 0
    fi
  done
  return 1
}

echo "== BEFORE =="
print_roles

OLD_PRIMARY="$(find_primary_service || true)"
if [ -z "${OLD_PRIMARY:-}" ]; then
  echo "No PRIMARY found in ${SHARD}."
  exit 1
fi

echo "== CURRENT PRIMARY =="
echo "$OLD_PRIMARY"

echo "== STOP PRIMARY: $OLD_PRIMARY =="
docker compose stop "$OLD_PRIMARY"

sleep 10

echo "== AFTER PRIMARY FAILURE =="
print_roles

NEW_PRIMARY="$(find_primary_service || true)"
echo "== NEW PRIMARY =="
echo "${NEW_PRIMARY:-NONE}"

echo "== QUERY THROUGH MONGOS AFTER PRIMARY FAILURE =="
docker compose exec -T mongos mongosh --quiet --port 27017 \
  -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" \
  --authenticationDatabase admin --eval '
    db = db.getSiblingDB("worlddb");
    print("co2", db.co2_country_year.countDocuments());
    print("happy", db.happiness_country_year.countDocuments());
    print("wdi", db.wdi_selected_long.countDocuments());
    print("master", db.country_year_master.countDocuments());
  '

echo "== START OLD PRIMARY: $OLD_PRIMARY =="
docker compose start "$OLD_PRIMARY"

sleep 10

echo "== AFTER RECOVERY =="
print_roles
