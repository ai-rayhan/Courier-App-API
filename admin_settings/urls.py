from django.urls import path
from admin_settings.views.delivery_times import DeliveryTimesList,DeliveryTimesDetail
from admin_settings.views.delivery_status import DeliveryStatusList,DeliveryStatusDetail,ParcelSummarybyStatus
from admin_settings.views.product_type import ProductTypeList,ProductTypeDetail
from admin_settings.views.sms_provider import SmsProviderList,SmsProviderDetail
from admin_settings.views.payment_settings import PaymentSettingsAPIView

urlpatterns = [
    path('delivery-time/', DeliveryTimesList.as_view(), name='deliverytime-list'),
    path('delivery-time/<int:pk>/', DeliveryTimesDetail.as_view(), name='deliverytime-detail'),

    path('product-type/', ProductTypeList.as_view(), name='product-type-list'),
    path('product-type/<int:pk>/', ProductTypeDetail.as_view(), name='product-type-detail'),

    path('delivery-status/', DeliveryStatusList.as_view(), name='deliverystatus-list'),
    path('delivery-status/<int:pk>/', DeliveryStatusDetail.as_view(), name='deliverystatus-detail'),
    path('ds-parcel-count/', ParcelSummarybyStatus.as_view(), name='deliverystatus-count-parcel'),
    
    path('sms-provider/', SmsProviderList.as_view(), name='sms-list'),
    path('sms-provider/<int:pk>/', SmsProviderDetail.as_view(), name='sms-detail'),
    path('payment-settings/', PaymentSettingsAPIView.as_view(), name='payment-settings'),

]
