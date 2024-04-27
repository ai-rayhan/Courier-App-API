from django.urls import path
from .views import DeliveryStatusList,DeliveryStatusDetail

urlpatterns = [
    path('delivery-status/', DeliveryStatusList.as_view(), name='deliverystatus-list'),
    path('delivery-status/<int:pk>/', DeliveryStatusDetail.as_view(), name='deliverystatus-detail'),
]
