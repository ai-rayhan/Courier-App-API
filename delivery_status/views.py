from delivery_status.models import DeliveryStatus,StatusTracking
from delivery_status.serializers import DeliveryStatusSerializer,StatusTrackingSerializer
from rest_framework import generics
from rest_framework import mixins
from webcourier.permissions import*
from rest_framework.permissions import  IsAuthenticated, IsAdminUser



class DeliveryStatusList(generics.ListCreateAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsAdminUser()]  
        return super().get_permissions()  
    
class DeliveryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsAdminUser()]
        return super().get_permissions()

class StatusTrackingList(generics.ListCreateAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]

    
class StatusTrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = StatusTrackingSerializer
    permission_classes = [IsAuthenticated]
