from parcels.models import ParcelDetails
from parcels.serializers import ParcelDetailsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ParcelDetailsList(generics.ListCreateAPIView):
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        parcel_id = self.request.query_params.get('parcel')
        if parcel_id is not None:
            queryset = ParcelDetails.objects.filter(parcel_id=parcel_id)
        else:
            queryset = ParcelDetails.objects.none()
        return queryset
    
class ParcelDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelDetails.objects.all()
    serializer_class = ParcelDetailsSerializer
    permission_classes = [IsAuthenticated]
