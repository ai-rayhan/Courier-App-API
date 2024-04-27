from rest_framework import serializers
from .models import DeliveryTimes,ProductType,DriverPayment,MerchantPayment

class DeliveryTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTimes
        fields = '__all__'
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
class DriverPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPayment
        fields = '__all__'
class MerchantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantPayment
        fields = '__all__'