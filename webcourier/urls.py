from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/merchants/', include('merchants.urls')),
    path('api/bank/', include('bank.urls')),
    path('api/parcels/', include('parcels.urls')),
    path('api/rider/', include('riders.urls')),
    path('api/receiver/', include('receiver.urls')),
    # path('api/deliverystatus/', include('delivery_status.urls')),
    path('api/branch/', include('branches.urls')),
    path('api/settings/', include('admin_settings.urls')),
    path('api/accounts/', include('accounts.urls')),
   
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)