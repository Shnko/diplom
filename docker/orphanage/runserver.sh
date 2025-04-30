#!/usr/bin/env bash

cd /app

echo Migration.
python manage.py migrate admin --noinput
python manage.py migrate auth --noinput
python manage.py migrate session --noinput

echo Init Admin.
python manage.py init_admin

echo Run Server
python manage.py runserver 0.0.0.0:8000