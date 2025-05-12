#!/usr/bin/env bash

cd /app

echo Migration.
python manage.py migrate

echo Init Admin.
python manage.py init_admin

echo Run Server
python manage.py runserver 0.0.0.0:8000