"""Development settings and globals."""


## Debug.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = (
	'127.0.0.1',
)

## Email.
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

## Site admins.
ADMINS = (
	('Randall Degges', 'rdegges@gmail.com'),
)
MANAGERS = ADMINS

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
SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
