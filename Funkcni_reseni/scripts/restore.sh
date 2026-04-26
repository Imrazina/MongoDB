#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
set -a
# shellcheck disable=SC1090
source "$COMPOSE_ROOT/.env"
set +a
cd "$COMPOSE_ROOT"
if [ $# -ne 1 ]; then
  echo "Usage: $0 backups/<timestamp>/worlddb.archive.gz"
  exit 1
fi
cat "$1" | docker compose exec -T mongos bash -lc "mongorestore --host localhost --port 27017 -u '$MDB_ADMIN_USER' -p '$MDB_ADMIN_PWD' --authenticationDatabase admin --nsInclude worlddb.* --drop --gzip --archive"
echo "Restore done from: $1"
