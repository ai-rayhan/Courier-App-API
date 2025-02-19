
from rest_framework import generics
from parcels.models import Parcel
from parcels.serializers import ParcelSerializer
from rest_framework.permissions import IsAuthenticated

class ParcelListByStatus(generics.ListCreateAPIView):
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        delivery_status_id = self.request.query_params.get('delivery_status')

        print(delivery_status_id)
        if delivery_status_id is not None:
            print(user_id)
            queryset = Parcel.objects.filter(driver_id=user_id, delivery_status_id=delivery_status_id)
        else:
            queryset = Parcel.objects.none()
        
        return queryset

class ParcelListByVoucherId(generics.ListCreateAPIView):
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        voucher_id = self.request.query_params.get('voucher_id')

        # If delivery_status_id is provided in query params, filter by it
        if voucher_id is not None:
            queryset = Parcel.objects.filter(driver_id=user_id, voucher_id=voucher_id)
        else:
            queryset = Parcel.objects.none()
        
        return queryset
