from django.urls import path
from parcels.views.parcels import ParcelUpdate,ParcelList,UpdateParcelStatus,RiderParcelUpdate,ParcelDetailView
from parcels.views.issues import IssueList,IssueDetail
from parcels.views.parcel_details import ParcelItemList,ParcelItemUpdate
from parcels.views.return_parcels import ReturnParcelList,ReturnParcelDetail
from parcels.views.status_tracking import ParcelStatusTrackingListView
# StatusTrackingList,StatusTrackingDetail,

urlpatterns = [
    path('list-create/', ParcelList.as_view(), name='list-create'),
    path('update-destroy/<int:pk>/', ParcelUpdate.as_view(), name='update-destroy'),
    path('parcel-details/<int:id>/', ParcelDetailView.as_view(), name='parcel-details'),

    path('rider-upadate/<int:pk>/', RiderParcelUpdate.as_view(), name='parceldetails-detail'),

    path('parceldetails/', ParcelItemList.as_view(), name='parceldetails-list'),
    path('parceldetails/<int:pk>/', ParcelItemUpdate.as_view(), name='parceldetails-detail'),

    path('update-status/', UpdateParcelStatus.as_view(), name='update-parcel'),
    
    path('returnparcel/', ReturnParcelList.as_view(), name='returnparcel-list'),
    path('returnparcel/<int:pk>/', ReturnParcelDetail.as_view(), name='returnparcel-detail'),

    path('issues/', IssueList.as_view(), name='issues-list'),
    path('issues/<int:pk>/', IssueDetail.as_view(), name='issues-detail'),

    # path('status-tracking/', StatusTrackingList.as_view(), name='statustracking-list'),
    # path('status-tracking/<int:pk>/', StatusTrackingDetail.as_view(), name='statustracking-detail'),

    path('tracking/<str:voucher_id>/', ParcelStatusTrackingListView.as_view(), name='statustracking-list'),



]
