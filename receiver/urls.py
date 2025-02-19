from django.urls import path
from .views import ReciverList, ReceverDetail

urlpatterns = [
    path('receivers/', ReciverList.as_view(), name='receiver-list'),
    path('receivers/<int:pk>/', ReceverDetail.as_view(), name='receiver-detail'),
]
