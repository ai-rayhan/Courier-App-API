from django.urls import path
from .views import DeliveryTimesList,ProductTypeList,DriverPaymentList,MerchantPaymentList
from .views import DeliveryTimesDetail,ProductTypeDetail,DriverPaymentDetail,MerchantPaymentDetail

urlpatterns = [
    path('delivery-time/', DeliveryTimesList.as_view(), name='deliverytime-list'),
    path('delivery-time/<int:pk>/', DeliveryTimesDetail.as_view(), name='deliverytime-detail'),

    path('product-type/', ProductTypeList.as_view(), name='product-type-list'),
    path('product-type/<int:pk>/', ProductTypeDetail.as_view(), name='product-type-detail'),
    
    path('driver-payment/', DriverPaymentList.as_view(), name='driver-payment-list'),
    path('driver-payment/<int:pk>/', DriverPaymentDetail.as_view(), name='driver-payment-detail'),

    path('merchant-payment/', MerchantPaymentList.as_view(), name='merchant-payment-list'),
    path('merchant-payment/<int:pk>/', MerchantPaymentDetail.as_view(), name='merchant-payment-detail'),
]
