"""Common settings and globals."""


import sys
from random import choice


## Important locations.
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
PROJECT_NAME = PROJECT_ROOT.name
SITE_ROOT = PROJECT_ROOT.dirname()
SECRET_FILE = SITE_ROOT / 'deploy' / 'SECRET'

## Setup the system path.
sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
sys.path.append(PROJECT_ROOT / 'libs')

## Debugging (off by default). DO NOT ENABLE IN PRODUCTION!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

## Admins and managers.
ADMINS = (
	('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

## Time zone (http://en.wikipedia.org/wiki/List_of_tz_zones_by_name).
TIME_ZONE = 'America/Los_Angeles'

## Language (http://www.i18nguy.com/unicode/language-identifiers.html).
LANGUAGE_CODE = 'en-us'

## Unique site identifier.
SITE_ID = 1

## Internationalization. Set to True if you want to support non-English
## languages.
USE_I18N = False

## Localize dates, numbers, and calendars.
USE_L10N = True

## User-uploaded media settings.
MEDIA_ROOT = PROJECT_ROOT / 'media'
MEDIA_URL = '/media/'

## Static file settings.
STATIC_ROOT = PROJECT_ROOT / 'static'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
	PROJECT_ROOT / 'assets',
)
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^yzyn-*r2!(w=eufdn642o*j47n2t&_l3!%0zj2%)p7+7)ok^v'

## Uploads.
FILE_UPLOAD_TEMP_DIR = SITE_ROOT / 'tmp'

## Cache.
CACHE_MIDDLEWARE_SECONDS = 60 * 30
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	  'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.http.ConditionalGetMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	PROJECT_ROOT / 'templates',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	## Admin panel and documentation.
	'django.contrib.admin',
	'django.contrib.admindocs',
)

def gen_secret_key(l):
	"""Generate a random secret key of length l."""

	return ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(l)])
