#!/usr/bin/env bash

set -e
if [ "$RUN_FLAG" = "DEMO" ]
then
  python manage.py makemigrations
  python manage.py migrate
  echo "from django.contrib.auth.models import User; "\
  "User.objects.create_superuser('test', 'drkydk@gmail.com', 'test')"\
  " if not User.objects.filter(username='test').exists() else ''"\
   | python manage.py shell
# daphne -b 0.0.0.0 djangoProject2.asgi:application
  python manage.py runserver 0.0.0.0:8000
else
  daphne -b 0.0.0.0 djangoProject2.asgi:application
fi

