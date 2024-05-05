from accounts.models import DriverPayment
from accounts.serializers import DriverPaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin

class DriverPaymentList(generics.ListCreateAPIView):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class DriverPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()