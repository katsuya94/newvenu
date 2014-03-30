from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'newvenu.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	
	url(r'^accounts/', include('allauth.urls')),

	url(r'^$', 'events.views.index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^events/', include('events.urls', namespace='events')),
)
