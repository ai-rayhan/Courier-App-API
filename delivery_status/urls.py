from django.urls import path
from .views import DeliveryStatusList,DeliveryStatusDetail
from .views import StatusTrackingList,StatusTrackingDetail

urlpatterns = [
    path('delivery-status/', DeliveryStatusList.as_view(), name='deliverystatus-list'),
    path('delivery-status/<int:pk>/', DeliveryStatusDetail.as_view(), name='deliverystatus-detail'),
    
    path('status-tracking/', StatusTrackingList.as_view(), name='statustracking-list'),
    path('status-tracking/<int:pk>/', StatusTrackingDetail.as_view(), name='statustracking-detail'),
]
