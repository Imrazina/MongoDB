#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPOSE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

set -a
# shellcheck disable=SC1090
source "$COMPOSE_ROOT/.env"
set +a

cd "$COMPOSE_ROOT"

echo "== MongoDB data, shard and chunk report =="
docker compose exec -T mongos mongosh --quiet --port 27017 \
  -u "$MDB_ADMIN_USER" -p "$MDB_ADMIN_PWD" \
  --authenticationDatabase admin --eval '
const dbw = db.getSiblingDB("worlddb");
const cfg = db.getSiblingDB("config");
const collections = [
  "co2_country_year",
  "happiness_country_year",
  "wdi_selected_long",
  "country_year_master"
];

for (const name of collections) {
  const ns = "worlddb." + name;
  const coll = dbw.getCollection(name);

  print("\n--- " + ns + " ---");
  print("documents:", coll.countDocuments());

  const stats = coll.stats();
  printjson({
    namespace: ns,
    sharded: stats.sharded,
    size_bytes: stats.size,
    storage_size_bytes: stats.storageSize,
    avg_object_size_bytes: stats.avgObjSize,
    index_size_bytes: stats.totalIndexSize
  });

  const perShardStats = {};
  if (stats.shards) {
    for (const [shardName, shardStats] of Object.entries(stats.shards)) {
      perShardStats[shardName] = {
        documents: shardStats.count,
        size_bytes: shardStats.size,
        storage_size_bytes: shardStats.storageSize,
        avg_object_size_bytes: shardStats.avgObjSize,
        index_size_bytes: shardStats.totalIndexSize
      };
    }
  }
  print("Per-shard statistics from coll.stats().shards:");
  printjson(perShardStats);

  print("Shard distribution from getShardDistribution():");
  coll.getShardDistribution();

  const meta = cfg.collections.findOne({_id: ns});
  if (meta) {
    const chunkQuery = meta.uuid ? {uuid: meta.uuid} : {ns: ns};
    const chunks = cfg.chunks.find(chunkQuery).sort({min: 1}).toArray();
    const byShard = {};
    for (const chunk of chunks) {
      byShard[chunk.shard] = (byShard[chunk.shard] || 0) + 1;
    }

    print("Chunk count:", chunks.length);
    printjson({chunks_by_shard: byShard});
    print("Chunk ranges and estimated chunk sizes:");
    for (const chunk of chunks.slice(0, 5)) {
      const shardChunkCount = byShard[chunk.shard] || 0;
      const shardSizeBytes = perShardStats[chunk.shard]?.size_bytes;
      const estimatedSizeBytes = shardChunkCount && shardSizeBytes !== undefined
        ? Math.round(shardSizeBytes / shardChunkCount)
        : "not available";
      printjson({
        shard: chunk.shard,
        min: chunk.min,
        max: chunk.max,
        estimated_method: "shard size divided by chunk count on the shard",
        estimated_size_bytes: estimatedSizeBytes
      });
    }
  } else {
    print("No metadata in config.collections for " + ns);
  }
}
'

echo
echo "== Replica set secondary replication info =="
for spec in "sh1a 27018 shard1RS" "sh2a 27018 shard2RS" "sh3a 27018 shard3RS"; do
  set -- $spec
  node="$1"
  port="$2"
  rs_name="$3"

  echo
  echo "--- $rs_name ($node) ---"
  docker compose exec -T "$node" bash -lc "
    SYSTEM_PWD=\"\$(tr -d '\n' < /keyfile/mongo-keyfile)\"
    mongosh --quiet --port '$port' \
      -u __system -p \"\$SYSTEM_PWD\" \
      --authenticationDatabase local --eval '
        rs.printSecondaryReplicationInfo();
      '
  "
done
