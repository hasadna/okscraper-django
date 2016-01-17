# encoding: utf-8

import logging, os

INSTALLED_APPS = [
    'okscraper_django'
]

SECRET_KEY = 'SECRET'

DATABASES = {
    'default': {
        'NAME': 'dev.db',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

ROOT_URLCONF = 'okscraper_django.urls'

if os.getenv('DJANGO', '') == "django":
    MIGRATION_MODULES = {
        'okscraper_django': 'okscraper_django.django_migrations',
    }
