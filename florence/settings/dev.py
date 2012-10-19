from os.path import normpath, join
from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'florence_local',
        'USER': 'root',
        'PASSWORD': 'Madison1',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'v)97yliekvu2j$x5w%&amp;$kkp8sr93_=7&amp;+4@9#bdw)pfr#&amp;ex@i'

MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
