#!/bin/sh
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_ADMIN_USER', '$DJANGO_ADMIN_EMAIL', '$DJANGO_ADMIN_PASSWORD')" | ./manage.py shell