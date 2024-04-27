from django.urls import path
from .views import ParcelList,IssueList,ParcelDetailsList,ReturnParcelList
from .views import ParcelDetail,IssueDetail,ParcelDetailsDetail,ReturnParcelDetail

urlpatterns = [
    path('parcels/', ParcelList.as_view(), name='parcel-list'),
    path('parcels/<int:pk>/', ParcelDetail.as_view(), name='parcel-detail'),

    path('issues/', IssueList.as_view(), name='issues-list'),
    path('issues/<int:pk>/', IssueDetail.as_view(), name='issues-detail'),

    path('parceldetails/', ParcelDetailsList.as_view(), name='parceldetails-list'),
    path('parceldetails/<int:pk>/', ParcelDetailsDetail.as_view(), name='parceldetails-detail'),

    path('returnparcel/', ReturnParcelList.as_view(), name='returnparcel-list'),
    path('returnparcel/<int:pk>/', ReturnParcelDetail.as_view(), name='returnparcel-detail'),
]
