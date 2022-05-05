"""
Django settings for disasterinfosite project.
"""
ADMINS = (
          ('Melinda Minch', 'melinda@melindaminch.com')
         )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
    SITE_URL= 'http://127.0.0.1:8000'
else:
    ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'embed_video',
    'disasterinfosite',
    'solo',
    'webpack_loader'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'disasterinfosite.urls'

WSGI_APPLICATION = 'disasterinfosite.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

### HEROKU CONFIGURATIONS ###
# Added per instructions at https://devcenter.heroku.com/articles/getting-started-with-django

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Allow database connections to persist
CONN_MAX_AGE = environ.get('CONN_MAX_AGE') or 0

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'build/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.map']
    }
}

FORCE_SCRIPT_NAME='/missoula/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
    # Use this setting if the app is being served at the domain root (e.g. hazardready.org/ )
    STATIC_URL = '/static/'
else:
    # If the app is being served in a subdirectory of the domain (e.g. foo.com/SUBDIR/ ) then use a variant of:
    # STATIC_URL = '/SUBDIR/static/'
    # So for our current test server, eldang.eldan.co.uk/zr/ , we need:
    # STATIC_URL = '/zr/static/'
    STATIC_URL = '/missoula/static/'

# STATIC_URL = '/missoula/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Specially for GeoDjango on Heroku
GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')

### ^^^^^^^^^^^^^^^^^^^^^^^^^ ###
### END HEROKU CONFIGURATIONS ###


MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'img')

if DEBUG:
    MEDIA_URL = '/staticfiles/img/'
else:
    MEDIA_URL = '/missoula/static/img/'
