from admin_settings.models import DeliveryTimes
from admin_settings.serializers import DeliveryTimesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin

class DeliveryTimesList(generics.ListCreateAPIView):
    queryset = DeliveryTimes.objects.all()
    serializer_class = DeliveryTimesSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions()  

class DeliveryTimesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryTimes.objects.all()
    serializer_class = DeliveryTimesSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()
