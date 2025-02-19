from accounts.models import RiderPayment
from accounts.serializers import DriverPaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin

class DriverPaymentList(generics.ListCreateAPIView):
    queryset = RiderPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class DriverPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RiderPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()