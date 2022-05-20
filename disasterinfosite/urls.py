from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth import login, logout

from disasterinfosite import views

urlpatterns = [
   path('', views.app_view),
   path('admin/', admin.site.urls),
   path('accounts/login/', login),
   path('accounts/logout/', logout),
   path('accounts/create_user/', views.create_user),
   path('accounts/update_profile/', views.update_profile)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
