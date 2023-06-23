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
python /web/manage.py runserver 143.42.59.132:9000
