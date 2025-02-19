from django.urls import path
from .views import BranchList,BranchDetail,DeliveryZoneList,DeliveryZoneDetail,PickupZoneList, PickupZoneDetail

urlpatterns = [
    path('branches/', BranchList.as_view(), name='branches-list'),
    path('branches/<int:pk>/', BranchDetail.as_view(), name='branches-detail'),
    path('delivery-zone/', DeliveryZoneList.as_view(), name='deliveryzone-list'),
    path('delivery-zone/<int:pk>/', DeliveryZoneDetail.as_view(), name='deliveryzone-detail'),
    path('pickup-zone/', PickupZoneList.as_view(), name='pickupzone-list'),
    path('pickup-zone/<int:pk>/', PickupZoneDetail.as_view(), name='pickupzone-detail'),
]
