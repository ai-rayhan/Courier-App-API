from parcels.models import ParcelItem
from parcels.serializers import ParcelItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ParcelItemList(generics.ListCreateAPIView):
    serializer_class = ParcelItemSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        parcel_id = self.request.query_params.get('parcel')
        if parcel_id is not None:
            queryset = ParcelItem.objects.filter(parcel_id=parcel_id)
        else:
            queryset = ParcelItem.objects.none()
        return queryset
    
class ParcelItemUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParcelItem.objects.all()
    serializer_class = ParcelItemSerializer
    permission_classes = [IsAuthenticated]
