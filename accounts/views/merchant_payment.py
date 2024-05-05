from accounts.models import MerchantPayment
from accounts.serializers import MerchantPaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin


class MerchantPaymentList(generics.ListCreateAPIView):
    queryset = MerchantPayment.objects.all()
    serializer_class = MerchantPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class MerchantPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MerchantPayment.objects.all()
    serializer_class = MerchantPaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()
