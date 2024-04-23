from django.urls import path
from .views import RiderList, RiderDetail

urlpatterns = [
    path('riders/', RiderList.as_view(), name='rider-list'),
    path('riders/<int:pk>/', RiderDetail.as_view(), name='riders-detail'),
]
