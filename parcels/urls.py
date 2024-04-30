from django.urls import path
from parcels.views.parcels import ParcelDetail,ParcelList,UpdateParcelStatus
from parcels.views.issues import IssueList,IssueDetail
from parcels.views.parcel_details import ParcelDetailsList,ParcelDetailsDetail
from parcels.views.return_parcels import ReturnParcelList,ReturnParcelDetail

urlpatterns = [
    path('parcels/', ParcelList.as_view(), name='parcel-list'),
    path('parcels/<int:pk>/', ParcelDetail.as_view(), name='parcel-detail'),
    
    path('parceldetails/', ParcelDetailsList.as_view(), name='parceldetails-list'),
    path('parceldetails/<int:pk>/', ParcelDetailsDetail.as_view(), name='parceldetails-detail'),

    path('update-status/<int:pk>/', UpdateParcelStatus.as_view(), name='update-parcel'),
    
    path('returnparcel/', ReturnParcelList.as_view(), name='returnparcel-list'),
    path('returnparcel/<int:pk>/', ReturnParcelDetail.as_view(), name='returnparcel-detail'),

    path('issues/', IssueList.as_view(), name='issues-list'),
    path('issues/<int:pk>/', IssueDetail.as_view(), name='issues-detail'),


]
