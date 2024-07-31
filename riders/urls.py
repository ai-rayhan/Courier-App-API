from django.urls import path
from riders.views.riders import RiderList, RiderDetail,RiderStatusUpdate,RiderDetails
from riders.views.rider_parcel import ParcelListByStatus, ParcelListByVoucherId

urlpatterns = [
    path('list-create/', RiderList.as_view(), name='rider-list'),
    path('update-destroy/<int:pk>/', RiderDetail.as_view(), name='riders-detail'),
    path('status/', RiderStatusUpdate.as_view(), name='riders-status'),
    path('admins-list/', RiderDetails.as_view(), name='admin-riders'),
    path('parcels-status/', ParcelListByStatus.as_view(), name='parcel-listby-status'),
    path('parcel-id/', ParcelListByVoucherId.as_view(), name='parcel-listby-id'),
]
