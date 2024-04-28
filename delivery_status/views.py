from delivery_status.models import DeliveryStatus,StatusTracking
from delivery_status.serializers import DeliveryStatusSerializer,StatusTrackingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class DeliveryStatusList(generics.ListCreateAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]

    
class DeliveryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]

class StatusTrackingList(generics.ListCreateAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]

    
class StatusTrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]
