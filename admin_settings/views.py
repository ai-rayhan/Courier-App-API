from .models import DeliveryTimes,ProductType,DriverPayment,MerchantPayment
from .serializers import DeliveryTimesSerializer,ProductTypeSerializer,DriverPaymentSerializer,MerchantPaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin,HasSpecificPermission

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

class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.filter(parent=None)
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()


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
