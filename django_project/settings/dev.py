"""Development settings and globals."""


from common import *
from os.path import join, normpath


########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': normpath(join(SITE_ROOT, 'db', 'default.db')),
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}
########## END DATABASE CONFIGURATION


## Key.
SECRET_KEY = gen_secret_key(50)
