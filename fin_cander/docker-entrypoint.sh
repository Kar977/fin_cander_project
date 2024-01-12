#!/bin/sh

# Wykonaj migracje przed uruchomieniem serwera
python manage.py makemigrations
python manage.py migrate

# Uruchom serwer Django
exec "$@"
