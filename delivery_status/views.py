from delivery_status.models import DeliveryStatus
from delivery_status.serializers import DeliveryStatusSerializer
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
