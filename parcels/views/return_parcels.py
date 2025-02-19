from parcels.models import ReturnParcel
from parcels.serializers import ReturnParcelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ReturnParcelList(generics.ListCreateAPIView):
    queryset = ReturnParcel.objects.all()
    serializer_class = ReturnParcelSerializer
    permission_classes = [IsAuthenticated]
class ReturnParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReturnParcel.objects.all()
    serializer_class = ReturnParcelSerializer
    permission_classes = [IsAuthenticated]

