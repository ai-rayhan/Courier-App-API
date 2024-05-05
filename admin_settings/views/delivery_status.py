from admin_settings.models import DeliveryStatus
from admin_settings.serializers import DeliveryStatusSerializer
from rest_framework import generics
from webcourier.permissions import IsSuperUserORAdmin
from rest_framework.permissions import  IsAuthenticated



class DeliveryStatusList(generics.ListCreateAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions()  
    
class DeliveryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()