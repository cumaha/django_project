"""Development settings and globals."""


DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
