from config.settings.production import DATABASES
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [

]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}