from parcels.models import ParcelDetails
from parcels.serializers import ParcelDetailsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ParcelDetailsList(generics.ListCreateAPIView):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]
class ParcelDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]
