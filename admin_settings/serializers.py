from rest_framework import serializers
from .models import DeliveryTimes,ProductType,DeliveryStatus,SmsProvider

class DeliveryTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTimes
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'
class SMSProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsProvider
        fields = '__all__'