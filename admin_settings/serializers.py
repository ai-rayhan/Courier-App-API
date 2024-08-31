from rest_framework import serializers
from .models import DeliveryTimes,ProductType,DeliveryStatus,SmsProvider
from .models import PaymentSettings
from .models import PaymentServiceProvider

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


class PaymentServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentServiceProvider
        fields = '__all__'

class PaymentSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSettings
        fields = '__all__'
