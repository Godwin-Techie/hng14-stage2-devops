#!/bin/bash
set -e

# Bring up stack
docker compose up -d --build

API_PORT=$(docker compose port api 8000 | cut -d: -f2)

for i in {1..20}; do
  if curl -f http://localhost:$API_PORT/; then
    echo "API is ready"
    break
  fi
  echo "Waiting for API..."
  sleep 5
done

curl http://localhost:$API_PORT/api/example



# Tear down
docker compose down
