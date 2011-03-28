"""Development settings and globals."""


from common import *


## Debug.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = (
	'127.0.0.1',
)

## Email.
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

## Database settings.
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': SITE_ROOT / 'db' / PROJECT_NAME+'.db',
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}

## Cache.
CACHE_BACKEND = 'dummy://'

## Key.
SECRET_KEY = gen_secret_key(50)
