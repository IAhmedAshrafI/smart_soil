#!/bin/sh

echo "Collect static files"
python /web/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /web/manage.py makemigrations  --merge --noinput

# Apply database migrations
echo "Apply database migrations"
python /web/manage.py migrate

echo "Run server"
python /web/manage.py runserver 0.0.0.0:9000
