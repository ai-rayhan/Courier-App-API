from django.urls import path

from .views import BankInformationListCreateAPIView,BankInformationRetrieveUpdateDestroyAPIView,PaymentMethodListCreateAPIView,PaymentMethodRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('bank-info/', BankInformationListCreateAPIView.as_view(), name='bank-info-list-create'),
    path('bank-info/<int:pk>/', BankInformationRetrieveUpdateDestroyAPIView.as_view(), name='bank-info-detail'),

    path('payment-method/', PaymentMethodListCreateAPIView.as_view(), name='payment-list-create'),
    path('payment-method/<int:pk>/', PaymentMethodRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]
