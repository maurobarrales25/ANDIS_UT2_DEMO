#!/bin/bash
set -e

host="$1"
shift

# Espera hasta que MySQL esté listo
until mysql -h "$host" -u"$DB_USER" -p"$DB_PASS" -e 'select 1'; do
  echo "Esperando a que MySQL esté listo..."
  sleep 2
done

# Ejecuta el comando que sigue
exec "$@"