import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SITE_ID = 1

USE_TZ = True

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

SECRET_KEY = '0'

ROOT_URLCONF = 'denormal_tests.urls'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'denormal',
    'denormal_tests.tests',
)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MIDDLEWARE_CLASSES = ()

denormal_IGNORE_MODELS = [
    'tests.IgnoredTestObj',
]
