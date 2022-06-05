SHELL := /bin/bash

help:
    @$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
    pip install -r requirement.txt

activate:
    pipenv shell

run:
    python manage.py runserver
celery:
    celery worker -A FYP --loglevel=INFO --pool=solo
migration:
    python manage.py makemigrations

migrate:
    python manage.py migrate

superuser:
    python manage.py createsuperuser

