from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings

from world import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cascadiaprepared.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'(?i)^zoneCheck', views.zoneCheck),
    (r'(?i)^snuggetCheck', views.snuggetCheck),  
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )