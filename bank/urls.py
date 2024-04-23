from django.urls import path
from .views import add_payment_mathod, update_payment_mathod,add_bank_information,update_bank_information

urlpatterns = [
    path('add/', add_payment_mathod, name='add_payment_mathod'),
    path('update/<int:pk>/', update_payment_mathod, name='update_payment_mathod'),

    path('add_bankinfo/', add_bank_information, name='add_bank_information'),
    path('update_bankinfo/<int:pk>/', update_bank_information, name='update_bank_information'),
]
