from .models import MoneyReceipt,Ledger
from .serializers import LedgerSerializer,MoneyReceiptSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class LedgerList(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    permission_classes = [IsAuthenticated]

class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    permission_classes = [IsAuthenticated]


class MoneyReceiptList(generics.ListCreateAPIView):
    queryset = MoneyReceipt.objects.all()
    serializer_class = MoneyReceiptSerializer
    permission_classes = [IsAuthenticated]

class MoneyReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyReceipt.objects.all()
    serializer_class = MoneyReceiptSerializer
    permission_classes = [IsAuthenticated]
