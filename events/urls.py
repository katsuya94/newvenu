from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'newvenu.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', 'events.views.index', name='index'),
	url(r'^create/$', 'events.views.create', name='create'),
	url(r'^(?P<event_id>\d+)/$', 'events.views.detail', name='detail'),
	# url(r'^(?P<event_id>\d+)/go/$', 'events.views.go', name='go'),
)