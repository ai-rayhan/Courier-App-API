from .models import DeliveryTimes,ProductType,DriverPayment,MerchantPayment
from .serializers import DeliveryTimesSerializer,ProductTypeSerializer,DriverPaymentSerializer,MerchantPaymentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class DeliveryTimesList(generics.ListCreateAPIView):
    queryset = DeliveryTimes.objects.all()
    serializer_class = DeliveryTimesSerializer
    permission_classes = [IsAuthenticated]

class DeliveryTimesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryTimes.objects.all()
    serializer_class = DeliveryTimesSerializer
    permission_classes = [IsAuthenticated]


class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]


class DriverPaymentList(generics.ListCreateAPIView):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]

class DriverPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer
    permission_classes = [IsAuthenticated]

class MerchantPaymentList(generics.ListCreateAPIView):
    queryset = MerchantPayment.objects.all()
    serializer_class = MerchantPaymentSerializer
    permission_classes = [IsAuthenticated]

class MerchantPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MerchantPayment.objects.all()
    serializer_class = MerchantPaymentSerializer
    permission_classes = [IsAuthenticated]
