"""Common settings and globals."""


import sys
from random import choice
from os.path import abspath


########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = abspath(__file__)

# Project name.
PROJECT_NAME = DJANGO_ROOT.name

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = DJANGO_ROOT.dirname()

# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this project is
# interpreted.
SECRET_FILE = SITE_ROOT / 'deploy' / 'SECRET'

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(DJANGO_ROOT / 'apps')
sys.path.append(DJANGO_ROOT / 'libs')
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# Disable debugging by default.
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = (
	('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


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


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_ROOT / 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = DJANGO_ROOT / 'static'

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images. Make sure to
# use a trailing slash.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files.
STATICFILES_DIRS = (
	DJANGO_ROOT / 'assets',
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION


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
	DJANGO_ROOT / 'templates',
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
