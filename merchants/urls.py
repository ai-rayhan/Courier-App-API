from django.urls import path
from merchants.views.merchants import create_merchant, update_merchant,add_shop,update_shop
from merchants.views.merchant_package import PackageList

urlpatterns = [
    path('create/', create_merchant, name='create_merchant'),
    path('update/<int:pk>/', update_merchant, name='update_merchant'),
    path('addshop/', add_shop),
    path('updateshop/<int:pk>/', update_shop),
    path('parcels/', PackageList.as_view(), name='package-list'),
]
