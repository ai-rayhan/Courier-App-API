from accounts.models import Ledger
from accounts.serializers import LedgerSerializer
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