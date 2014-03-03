# encoding: utf-8

import logging

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
