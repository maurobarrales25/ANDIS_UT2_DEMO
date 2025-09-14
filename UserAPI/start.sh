#!/bin/sh
# wait-for-keycloak.sh
set -e
KEYCLOAK=${KEYCLOAK_URL:-http://keycloak:8080}
REALM_PATH="/realms/${KEYCLOAK_REALM:-demo-realm}"

echo "Waiting for Keycloak at ${KEYCLOAK}${REALM_PATH}..."
until curl -s "${KEYCLOAK}${REALM_PATH}" >/dev/null 2>&1; do
  echo "Keycloak not ready yet. Sleeping 2s..."
  sleep 2
done

echo "Keycloak is up — starting uvicorn"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload