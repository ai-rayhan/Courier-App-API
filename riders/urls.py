from django.urls import path
from riders.views.riders import RiderList,RiderActivate,RiderDetails,UpdateRider
from riders.views.rider_parcel import ParcelListByStatus, ParcelListByVoucherId

urlpatterns = [
    path('list-create/', RiderList.as_view(), name='rider-list'),
    path('update/<int:pk>/', UpdateRider.as_view(), name='riders-upadate'),
    path('riderdetails/<int:rider_id>/', RiderDetails.as_view(), name='riders-detail'),
    path('activate/', RiderActivate.as_view(), name='riders-status'),
    path('parcels-status/', ParcelListByStatus.as_view(), name='parcel-listby-status'),
    path('parcel-id/', ParcelListByVoucherId.as_view(), name='parcel-listby-id'),
]
