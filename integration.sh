#!/bin/bash
set -e

# Bring up stack
docker compose up -d --build

# Wait for API to be healthy
for i in {1..20}; do
  if docker compose exec -T api curl -f http://localhost:8000; then
    echo "API is ready"
    break
  fi
  echo "Waiting for API..."
  sleep 5
done

# Run integration test
docker compose exec -T api curl http://localhost:8000/api/example

# Tear down
docker compose down
