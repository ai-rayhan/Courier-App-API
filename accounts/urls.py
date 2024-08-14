from django.urls import path
from accounts.views.money_receipt import MoneyReceiptList,MoneyReceiptDetail
from accounts.views.ledger import LedgerList,LedgerDetail
from accounts.views.merchant_payment import MerchantPaymentDetail,MerchantPaymentList,PaymentListByMerchant
from accounts.views.driver_payment import DriverPaymentDetail,DriverPaymentList

urlpatterns = [
    path('moneyreceipt/', MoneyReceiptList.as_view(), name='moneyreceipt-list'),
    path('moneyreceipt/<int:pk>/', MoneyReceiptDetail.as_view(), name='moneyreceipt-detail'),

    path('ledger/', LedgerList.as_view(), name='ledger-list'),
    path('ledger/<int:pk>/', LedgerDetail.as_view(), name='ledger-detail'),

    path('driver-payment/', DriverPaymentList.as_view(), name='driver-payment-list'),
    path('driver-payment/<int:pk>/', DriverPaymentDetail.as_view(), name='driver-payment-detail'),

    path('merchant-payment/', MerchantPaymentList.as_view(), name='merchant-payment-list'),
    path('merchant-payment/<int:pk>/', MerchantPaymentDetail.as_view(), name='merchant-payment-detail'),
    path('payment-by-merchant/<int:merchantid>/', PaymentListByMerchant.as_view(), name='payment-by-merchant'),
]
