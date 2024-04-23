from django.urls import path
from .views import PackageList, PackageDetail

urlpatterns = [
    path('packages/', PackageList.as_view(), name='package-list'),
    path('packages/<int:pk>/', PackageDetail.as_view(), name='package-detail'),
]
