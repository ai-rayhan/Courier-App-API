from django.urls import path
from .views import create_merchant, update_merchant,add_shop,update_shop,PackageList

urlpatterns = [
    path('create/', create_merchant, name='create_merchant'),
    path('update/<int:pk>/', update_merchant, name='update_merchant'),
    path('addshop/', add_shop),
    path('updateshop/<int:pk>/', update_shop),
    path('packages/', PackageList.as_view(), name='package-list'),
]
