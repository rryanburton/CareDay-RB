from .settings import *
import os
import dj_database_url

DEBUG = False
DEBUG = bool(int(os.environ.get('DEBUG', True)))
SECRET_KEY = os.environ['SECRET_KEY']

BLACKLIST_APPS = ['debugtoolbar', 'django_extensions']

INSTALLED_APPS = tuple(
    [app for app in INSTALLED_APPS if app not in BLACKLIST_APPS])

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
