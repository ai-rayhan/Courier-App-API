from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/merchants/', include('merchants.urls')),
    path('api/bank/', include('bank.urls')),
    path('api/package/', include('packages.urls')),
    path('api/rider/', include('riders.urls')),
    path('api/receiver/', include('receiver.urls')),
   
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)