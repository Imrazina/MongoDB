#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
set -a
# shellcheck disable=SC1090
source "$COMPOSE_ROOT/.env"
set +a
cd "$COMPOSE_ROOT"
ts=$(date +%F_%H-%M-%S)
mkdir -p backups/$ts
docker compose exec -T mongos bash -lc "mongodump --host localhost --port 27017 --readPreference=primary -u '$MDB_ADMIN_USER' -p '$MDB_ADMIN_PWD' --authenticationDatabase admin --db worlddb --gzip --archive" > "backups/$ts/worlddb.archive.gz"
echo "Backup: backups/$ts/worlddb.archive.gz"
