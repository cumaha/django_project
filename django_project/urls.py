from django.contrib import admin
from django.conf.urls.defaults import include, patterns, url


admin.autodiscover()
urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'django_project.views.home', name='home'),
	# url(r'^django_project/', include('django_project.foo.urls')),

	# Admin panel and documentation.
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
