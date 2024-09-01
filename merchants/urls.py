from django.urls import path
from merchants.views.merchants import ShopList,ShopByMerchant,UpdateShop,MerchantActivate,Merchants,MerchantDetails,UpdateMerchant
urlpatterns = [
    path('merchant/', Merchants.as_view(), name='merchant-list'),
    path('merchant/<int:merchant_id>/', MerchantDetails.as_view(), name='merchant-details'),
    path('merchant/update/<int:pk>/', UpdateMerchant.as_view()),
    path('activate/', MerchantActivate.as_view(), name='merchant-activate'),
  
    path('allshop/', ShopList.as_view(),name='allshop'),
    path('shop-update/<int:pk>/', UpdateShop.as_view()),
    path('shop/', ShopByMerchant.as_view(),name='shops-merchants'),
]
