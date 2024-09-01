from django.urls import path
from parcels.views.parcels import ParcelUpdate,ParcelList,UpdateParcelStatus,ParcelDetailView,GetParcels
from parcels.views.issues import IssueList,IssueDetail
from parcels.views.parcel_details import ParcelItemList,ParcelItemUpdate
from parcels.views.return_parcels import ReturnParcelList,ReturnParcelDetail
from parcels.views.status_tracking import ParcelStatusTrackingListView
from parcels.views.parcel_summary import MerchantParcelSummaryView,RiderParcelSummaryView
from parcels.views.make_payment import MakeMerchantPayment,MakeRiderPayment

urlpatterns = [
    # Parcel
    path('list-create/', ParcelList.as_view(), name='list-create'),#deprecated 
    path('update-destroy/<int:pk>/', ParcelUpdate.as_view(), name='update-destroy'),
    path('getparcels/', GetParcels.as_view(), name='getparcels'),
    path('parcel-details/<int:id>/', ParcelDetailView.as_view(), name='parcel-details'),
    # Update status
    path('update-status/', UpdateParcelStatus.as_view(), name='update-parcel'),
    # Status tracking
    path('tracking/<str:voucher_id>/', ParcelStatusTrackingListView.as_view(), name='statustracking-list'),
    # ParcelItem
    path('parceldetails/', ParcelItemList.as_view(), name='parceldetails-list'),
    path('parceldetails/<int:pk>/', ParcelItemUpdate.as_view(), name='parceldetails-detail'),
    # Return parcel
    path('returnparcel/', ReturnParcelList.as_view(), name='returnparcel-list'),
    path('returnparcel/<int:pk>/', ReturnParcelDetail.as_view(), name='returnparcel-detail'),
    # issues
    path('issues/', IssueList.as_view(), name='issues-list'),
    path('issues/<int:pk>/', IssueDetail.as_view(), name='issues-detail'),
    # Parcel Summary
    path('merchant-parcel-summary/<int:merchant_id>/', MerchantParcelSummaryView.as_view(), name='merchant-parcel-summary'),
    path('rider-parcel-summary/<int:rider_id>/', RiderParcelSummaryView.as_view(), name='rider-parcel-summary'),
    # Payment for parcel
    path('merchant-payment/', MakeMerchantPayment.as_view(), name='merchant-payment'),
    path('rider-payment/', MakeRiderPayment.as_view(), name='rider-payment'),

]
