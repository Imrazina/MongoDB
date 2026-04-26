#!/usr/bin/env bash
set -euo pipefail

: "${MDB_ADMIN_USER:?MDB_ADMIN_USER is required}"
: "${MDB_ADMIN_PWD:?MDB_ADMIN_PWD is required}"
: "${MDB_APP_USER:?MDB_APP_USER is required}"
: "${MDB_APP_PWD:?MDB_APP_PWD is required}"
INIT_WAIT_SECONDS="${INIT_WAIT_SECONDS:-1800}"

if [ ! -s /keyfile/mongo-keyfile ]; then
  echo "[init] missing /keyfile/mongo-keyfile for __system auth" >&2
  exit 1
fi

SYSTEM_PWD="$(tr -d '\n' < /keyfile/mongo-keyfile)"

wait_mongo() {
  local host="$1"
  local port="$2"
  local name="$3"
  local waited=0

  while [ "$waited" -lt "$INIT_WAIT_SECONDS" ]; do
    local out=""
    out="$(mongosh --host "$host" --port "$port" --quiet --eval 'db.adminCommand({ ping: 1 })' 2>&1 || true)"
    if printf '%s' "$out" | grep -Eq 'ok[: ]+1|requires authentication|Authentication failed'; then
      echo "[init] $name is reachable"
      return 0
    fi

    out="$(mongosh --host "$host" --port "$port" -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval 'db.adminCommand({ ping: 1 })' 2>&1 || true)"
    if printf '%s' "$out" | grep -Eq 'ok[: ]+1|requires authentication|Authentication failed'; then
      echo "[init] $name is reachable"
      return 0
    fi
    sleep 2
    waited=$((waited + 2))
  done

  echo "[init] timeout waiting for $name after ${INIT_WAIT_SECONDS}s" >&2
  exit 1
}

wait_mongo cfg1 27019 cfg1
wait_mongo sh1a 27018 sh1a
wait_mongo sh2a 27018 sh2a
wait_mongo sh3a 27018 sh3a

mongosh --host cfg1 --port 27019 -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval 'try{rs.initiate({_id:"cfgRS",configsvr:true,members:[{_id:0,host:"cfg1:27019"},{_id:1,host:"cfg2:27019"},{_id:2,host:"cfg3:27019"}]})}catch(e){print(e.message)}'
mongosh --host sh1a --port 27018 -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval 'try{rs.initiate({_id:"shard1RS",members:[{_id:0,host:"sh1a:27018"},{_id:1,host:"sh1b:27018"},{_id:2,host:"sh1c:27018"}]})}catch(e){print(e.message)}'
mongosh --host sh2a --port 27018 -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval 'try{rs.initiate({_id:"shard2RS",members:[{_id:0,host:"sh2a:27018"},{_id:1,host:"sh2b:27018"},{_id:2,host:"sh2c:27018"}]})}catch(e){print(e.message)}'
mongosh --host sh3a --port 27018 -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval 'try{rs.initiate({_id:"shard3RS",members:[{_id:0,host:"sh3a:27018"},{_id:1,host:"sh3b:27018"},{_id:2,host:"sh3c:27018"}]})}catch(e){print(e.message)}'

sleep 10
wait_mongo mongos 27017 mongos

mongosh --host cfg1 --port 27019 -u __system -p "$SYSTEM_PWD" --authenticationDatabase local --quiet --eval "
db = db.getSiblingDB('admin');
if (!db.getUser('$MDB_ADMIN_USER')) {
  db.createUser({ user: '$MDB_ADMIN_USER', pwd: '$MDB_ADMIN_PWD', roles: [{ role: 'root', db: 'admin' }] });
}
"

mongosh --host mongos --port 27017 -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" --authenticationDatabase admin --quiet --eval "
try{sh.addShard('shard1RS/sh1a:27018,sh1b:27018,sh1c:27018')}catch(e){print(e.message)}
try{sh.addShard('shard2RS/sh2a:27018,sh2b:27018,sh2c:27018')}catch(e){print(e.message)}
try{sh.addShard('shard3RS/sh3a:27018,sh3b:27018,sh3c:27018')}catch(e){print(e.message)}
try{sh.enableSharding('worlddb')}catch(e){print(e.message)}

db = db.getSiblingDB('worlddb');
if (!db.getUser('$MDB_APP_USER')) {
  db.createUser({ user: '$MDB_APP_USER', pwd: '$MDB_APP_PWD', roles: [{ role: 'readWrite', db: 'worlddb' }, { role: 'dbAdmin', db: 'worlddb' }] });
}

if (!db.getCollectionNames().includes('country_year_master')) db.createCollection('country_year_master',{validator:{\$jsonSchema:{bsonType:'object',required:['iso3','year'],properties:{iso3:{bsonType:'string',minLength:3,maxLength:3},year:{bsonType:['int','long','double']},country:{bsonType:'string'},happiness_score:{bsonType:['int','long','double','null']},gdp_per_capita_usd:{bsonType:['int','long','double','null']},co2_per_capita_t:{bsonType:['int','long','double','null']}}}}});
if (!db.getCollectionNames().includes('co2_country_year')) db.createCollection('co2_country_year',{validator:{\$jsonSchema:{bsonType:'object',required:['iso3','year'],properties:{iso3:{bsonType:'string',minLength:3,maxLength:3},year:{bsonType:['int','long','double']},country:{bsonType:'string'},co2_per_capita_t:{bsonType:['int','long','double','null']},co2_total_mt:{bsonType:['int','long','double','null']}}}}});
if (!db.getCollectionNames().includes('happiness_country_year')) db.createCollection('happiness_country_year',{validator:{\$jsonSchema:{bsonType:'object',required:['iso3','year'],properties:{iso3:{bsonType:'string',minLength:3,maxLength:3},year:{bsonType:['int','long','double']},country:{bsonType:'string'},happiness_score:{bsonType:['int','long','double','null']}}}}});
if (!db.getCollectionNames().includes('wdi_selected_long')) db.createCollection('wdi_selected_long',{validator:{\$jsonSchema:{bsonType:'object',required:['iso3','year','indicator'],properties:{iso3:{bsonType:'string',minLength:3,maxLength:3},year:{bsonType:['int','long','double']},country:{bsonType:'string'},indicator:{bsonType:'string'},value:{bsonType:['int','long','double','null']}}}}});

db.country_year_master.createIndex({iso3:1,year:1});
db.co2_country_year.createIndex({iso3:1,year:1});
db.happiness_country_year.createIndex({iso3:1,year:1});
db.wdi_selected_long.createIndex({iso3:1,year:1,indicator:1});

try{sh.shardCollection('worlddb.country_year_master',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.co2_country_year',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.happiness_country_year',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.wdi_selected_long',{iso3:1,year:1,indicator:1})}catch(e){print(e.message)}
"

echo "[init] cluster initialization complete"
