from django.urls import path
from .views import MoneyReceiptList,LedgerList
from .views import MoneyReceiptDetail,LedgerDetail

urlpatterns = [
    path('moneyreceipt/', MoneyReceiptList.as_view(), name='moneyreceipt-list'),
    path('moneyreceipt/<int:pk>/', MoneyReceiptDetail.as_view(), name='moneyreceipt-detail'),

    path('ledger/', LedgerList.as_view(), name='ledger-list'),
    path('ledger/<int:pk>/', LedgerDetail.as_view(), name='ledger-detail'),
]
