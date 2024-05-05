from django.urls import path
from parcels.views.parcels import ParcelDetail,ParcelList,UpdateParcelStatus,RiderParcelUpdate
from parcels.views.issues import IssueList,IssueDetail
from parcels.views.parcel_details import ParcelDetailsList,ParcelDetailsDetail
from parcels.views.return_parcels import ReturnParcelList,ReturnParcelDetail
from parcels.views.status_tracking import StatusTrackingList,StatusTrackingDetail

urlpatterns = [
    path('list-create/', ParcelList.as_view(), name='list-create'),
    path('update-destroy/<int:pk>/', ParcelDetail.as_view(), name='update-destroy'),
    
    path('parceldetails/', ParcelDetailsList.as_view(), name='parceldetails-list'),
    path('parceldetails/<int:pk>/', ParcelDetailsDetail.as_view(), name='parceldetails-detail'),

    path('rider-upadate/<int:pk>/', RiderParcelUpdate.as_view(), name='parceldetails-detail'),

    path('update-status/<int:pk>/', UpdateParcelStatus.as_view(), name='update-parcel'),
    
    path('returnparcel/', ReturnParcelList.as_view(), name='returnparcel-list'),
    path('returnparcel/<int:pk>/', ReturnParcelDetail.as_view(), name='returnparcel-detail'),

    path('issues/', IssueList.as_view(), name='issues-list'),
    path('issues/<int:pk>/', IssueDetail.as_view(), name='issues-detail'),

    path('status-tracking/', StatusTrackingList.as_view(), name='statustracking-list'),
    path('status-tracking/<int:pk>/', StatusTrackingDetail.as_view(), name='statustracking-detail'),


]
