from parcels.models import StatusTracking
from parcels.serializers import StatusTrackingSerializer
from admin_settings.models import DeliveryStatus
from rest_framework import generics
# from webcourier.permissions import IsSuperUserORAdmin,HasSpecificPermission
from rest_framework.permissions import  IsAuthenticated

class StatusTrackingList(generics.ListCreateAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]

    
class StatusTrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]
