#!/bin/sh

echo "Changing directory..."
cd webapp

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn webapp.wsgi:application --bind 0.0.0.0:$PORT