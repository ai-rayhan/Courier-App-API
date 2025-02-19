from parcels.models import StatusTracking
from parcels.serializers import StatusTrackingSerializer
from admin_settings.models import DeliveryStatus
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status

class StatusTrackingList(generics.ListCreateAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]

class StatusTrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]

class ParcelStatusTrackingListView(APIView):
    def get(self, request, voucher_id):
        status_trackings = StatusTracking.objects.filter(parcel__voucher_id=voucher_id)
        serializer = StatusTrackingSerializer(status_trackings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 