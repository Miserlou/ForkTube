from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'ForkTube.forker.views.root'),
     url(r'^forking/(?P<hash>[^/]+)$', 'ForkTube.forker.views.forking'),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'../static'}),
     (r'^captcha/', include('captcha.urls')),
#     url(r'^admin/', include(admin.site.urls)),
)
