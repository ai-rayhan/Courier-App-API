from django.urls import path
from riders.views.riders import RiderList, RiderDetail
from riders.views.rider_parcel import ParcelListByStatus, ParcelListByVoucherId

urlpatterns = [
    path('list-create/', RiderList.as_view(), name='rider-list'),
    path('update-destroy/<int:pk>/', RiderDetail.as_view(), name='riders-detail'),
    path('parcels-status/', ParcelListByStatus.as_view(), name='parcel-listby-status'),
    path('parcel-id/', ParcelListByVoucherId.as_view(), name='parcel-listby-id'),
]
