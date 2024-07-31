from django.urls import path
from merchants.views.merchants import create_merchant, update_merchant,ShopList,ShopByMerchant,UpdateShop,MerchantList,MerchantActivate
from merchants.views.merchant_package import PackageListByStatus,PackageListByVoucherId,ParcelList

urlpatterns = [
    path('create/', create_merchant, name='create_merchant'),
    path('update/<int:pk>/', update_merchant, name='update_merchant'),
    path('allmerchants/', MerchantList.as_view(), name='merchant-list'),
    path('activate/', MerchantActivate.as_view(), name='merchant-activate'),
    path('allshop/', ShopList.as_view(),name='allshop'),
    path('shop-update/<int:pk>/', UpdateShop.as_view()),
    path('shop/', ShopByMerchant.as_view(),name='shops-merchants'),
    path('parcels/', ParcelList.as_view(), name='parcel-listby-status'),
    path('parcels-status/', PackageListByStatus.as_view(), name='parcel-listby-status'),
    path('parcel-id/', PackageListByVoucherId.as_view(), name='parcel-listby-id'),
]
