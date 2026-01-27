#!/bin/bash
set -e

echo "Starting Django Tutorial"
sleep 15
cd /app/
# Migraciones
python3 manage.py migrate --noinput

# Crear superusuario (no falla si ya existe)
python3 manage.py createsuperuser --noinput || true
# || true evita errores si el superusuario ya está creado
# Servidor de desarrollo
exec python3 manage.py runserver 0.0.0.0:8000
