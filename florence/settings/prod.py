import os
from common import *

DB_PASSWORD = os.getenv('DJ_DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'florence',
        'USER': 'florence_db',
        'PASSWORD': DB_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = os.getenv('DJ_SECRET_KEY')

## TODO: Fill me in
MEDIA_ROOT = ''
STATIC_ROOT = ''

AKISMET_SECRET_API_KEY = ""
