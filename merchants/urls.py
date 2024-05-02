from django.urls import path
from merchants.views.merchants import create_merchant, update_merchant,add_shop,update_shop
from merchants.views.merchant_package import PackageListByStatus,PackageListByVoucherId

urlpatterns = [
    path('create/', create_merchant, name='create_merchant'),
    path('update/<int:pk>/', update_merchant, name='update_merchant'),
    path('addshop/', add_shop),
    path('updateshop/<int:pk>/', update_shop),
    path('parcels-status/', PackageListByStatus.as_view(), name='parcel-listby-status'),
    path('parcel-id/', PackageListByVoucherId.as_view(), name='parcel-listby-id'),
]
