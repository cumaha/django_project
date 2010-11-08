"""Development settings and globals."""


DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
