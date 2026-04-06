#!/usr/bin/env bash
set -euo pipefail
source ~/.bsqbd_world_env
cd ~/BSQBD_ShabossovaAnna/Funkcni_reseni
ts=$(date +%F_%H-%M-%S)
mkdir -p backups/$ts
docker compose exec -T mongos bash -lc "mongodump --host localhost --port 27017 --readPreference=primary -u '$MDB_ADMIN_USER' -p '$MDB_ADMIN_PWD' --authenticationDatabase admin --db worlddb --gzip --archive" > "backups/$ts/worlddb.archive.gz"
echo "Backup: backups/$ts/worlddb.archive.gz"
