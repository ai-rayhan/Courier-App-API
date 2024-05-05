from accounts.models import MoneyReceipt
from accounts.serializers import MoneyReceiptSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class MoneyReceiptList(generics.ListCreateAPIView):
    queryset = MoneyReceipt.objects.all()
    serializer_class = MoneyReceiptSerializer
    permission_classes = [IsAuthenticated]

class MoneyReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyReceipt.objects.all()
    serializer_class = MoneyReceiptSerializer
    permission_classes = [IsAuthenticated]
