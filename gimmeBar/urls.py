from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from gimmeBar.views import *
from django.conf import settings


urlpatterns = patterns('',
	(r'^$', landing),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
)
