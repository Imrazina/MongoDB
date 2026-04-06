#!/usr/bin/env bash
set -e
cd ~/BSQBD_ShabossovaAnna/Funkcni_reseni
docker compose up -d
./scripts/check_cluster.sh
