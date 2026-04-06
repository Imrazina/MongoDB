#!/usr/bin/env bash
set -euo pipefail
cd ~/BSQBD_ShabossovaAnna/Funkcni_reseni
source ~/.bsqbd_world_env

docker compose up -d
sleep 8

docker compose exec -T cfg1 mongosh --port 27019 --eval 'try{rs.initiate({_id:"cfgRS",configsvr:true,members:[{_id:0,host:"cfg1:27019"},{_id:1,host:"cfg2:27019"},{_id:2,host:"cfg3:27019"}]})}catch(e){print(e.message)}'
docker compose exec -T sh1a mongosh --port 27018 --eval 'try{rs.initiate({_id:"shard1RS",members:[{_id:0,host:"sh1a:27018"},{_id:1,host:"sh1b:27018"},{_id:2,host:"sh1c:27018"}]})}catch(e){print(e.message)}'
docker compose exec -T sh2a mongosh --port 27018 --eval 'try{rs.initiate({_id:"shard2RS",members:[{_id:0,host:"sh2a:27018"},{_id:1,host:"sh2b:27018"},{_id:2,host:"sh2c:27018"}]})}catch(e){print(e.message)}'
docker compose exec -T sh3a mongosh --port 27018 --eval 'try{rs.initiate({_id:"shard3RS",members:[{_id:0,host:"sh3a:27018"},{_id:1,host:"sh3b:27018"},{_id:2,host:"sh3c:27018"}]})}catch(e){print(e.message)}'
sleep 10

docker compose exec -T mongos mongosh --port 27017 --eval "db.getSiblingDB('admin').createUser({user:'$MDB_ADMIN_USER',pwd:'$MDB_ADMIN_PWD',roles:[{role:'root',db:'admin'}]})" || true

docker compose exec -T mongos mongosh --port 27017 -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" --authenticationDatabase admin --eval "
try{sh.addShard('shard1RS/sh1a:27018,sh1b:27018,sh1c:27018')}catch(e){print(e.message)}
try{sh.addShard('shard2RS/sh2a:27018,sh2b:27018,sh2c:27018')}catch(e){print(e.message)}
try{sh.addShard('shard3RS/sh3a:27018,sh3b:27018,sh3c:27018')}catch(e){print(e.message)}
sh.enableSharding('worlddb');

db=db.getSiblingDB('worlddb');
if(!db.getUser('$MDB_APP_USER')) db.createUser({user:'$MDB_APP_USER',pwd:'$MDB_APP_PWD',roles:[{role:'readWrite',db:'worlddb'},{role:'dbAdmin',db:'worlddb'}]});

if(!db.getCollectionNames().includes('country_year_master')) db.createCollection('country_year_master',{validator:{\$jsonSchema:{bsonType:'object',required:['iso3','year'],properties:{iso3:{bsonType:'string',minLength:3,maxLength:3},year:{bsonType:['int','long','double']}}}}});
if(!db.getCollectionNames().includes('co2_country_year')) db.createCollection('co2_country_year');
if(!db.getCollectionNames().includes('happiness_country_year')) db.createCollection('happiness_country_year');
if(!db.getCollectionNames().includes('wdi_selected_long')) db.createCollection('wdi_selected_long');

db.country_year_master.createIndex({iso3:1,year:1});
db.co2_country_year.createIndex({iso3:1,year:1});
db.happiness_country_year.createIndex({iso3:1,year:1});
db.wdi_selected_long.createIndex({iso3:1,year:1,indicator:1});

try{sh.shardCollection('worlddb.country_year_master',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.co2_country_year',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.happiness_country_year',{iso3:1,year:1})}catch(e){print(e.message)}
try{sh.shardCollection('worlddb.wdi_selected_long',{iso3:1,year:1,indicator:1})}catch(e){print(e.message)}
"

~/BSQBD_ShabossovaAnna/.venv/bin/python ~/BSQBD_ShabossovaAnna/Funkcni_reseni/scripts/import_processed.py
~/BSQBD_ShabossovaAnna/Funkcni_reseni/scripts/check_cluster.sh
