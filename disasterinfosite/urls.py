from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth.views import login, logout

from disasterinfosite import views

urlpatterns = patterns('',
                       url(r'^$', views.app_view, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$',  login),
                       url(r'^accounts/logout/$', logout)
                       )

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve'),
                            )
