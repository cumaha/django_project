"""Staging settings and globals."""


from common import *


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[%s->STAGING] ' % SITE_NAME
EMAIL_USE_TLS = False
SERVER_EMAIL = 'root@localhost'
########## END EMAIL CONFIGURATION


## Database settings.
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '',						 # Or path to database file if using sqlite3.
		'USER': '',						 # Not used with sqlite3.
		'PASSWORD': '',					 # Not used with sqlite3.
		'HOST': '',						 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
	}
}

## Cache.
CACHE_BACKEND = 'file://%s' % (SITE_ROOT / 'cache' / PROJECT_NAME)

## Key.
try:
	SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
	try:
		with open(SECRET_FILE, 'w') as f:
			f.write(gen_secret_key(50))
	except IOError:
		raise Exception('Cannot open file %s for writing.' % SECRET_FILE)
