from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from disasterinfosite import views

urlpatterns = [
   url(r'^$', views.app_view),
   url(r'^admin/', admin.site.urls),
   url(r'^accounts/login/$',  LoginView),
   url(r'^accounts/logout/$', LogoutView),
   url(r'^accounts/create_user/$', views.create_user),
   url(r'^accounts/update_profile/$', views.update_profile)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
