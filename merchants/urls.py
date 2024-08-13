from django.urls import path
from merchants.views.merchants import ShopList,ShopByMerchant,UpdateShop,MerchantActivate,Merchants,MerchantDetails,UpdateMerchant
# from merchants.views.merchant_package import PackageListByStatus,PackageListByVoucherId,ParcelList
# create_merchant, update_merchant,
urlpatterns = [
    # path('create/', create_merchant, name='create_merchant'),
    # path('update/<int:pk>/', update_merchant, name='update_merchant'),

    path('allmerchants/', Merchants.as_view(), name='merchant-list'),
    path('merchant/<int:merchant_id>/', MerchantDetails.as_view(), name='merchant-details'),
    path('activate/', MerchantActivate.as_view(), name='merchant-activate'),
    path('update/<int:pk>/', UpdateMerchant.as_view()),

    path('allshop/', ShopList.as_view(),name='allshop'),
    path('shop-update/<int:pk>/', UpdateShop.as_view()),
    path('shop/', ShopByMerchant.as_view(),name='shops-merchants'),
    # path('parcels/', ParcelList.as_view(), name='parcel-listby-status'),
    # path('parcels-status/', PackageListByStatus.as_view(), name='parcel-listby-status'),
    # path('parcel-id/', PackageListByVoucherId.as_view(), name='parcel-listby-id'),
]
