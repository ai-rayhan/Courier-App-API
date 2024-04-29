from rest_framework import serializers
from .models import DeliveryTimes,ProductType,DriverPayment,MerchantPayment

class DeliveryTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTimes
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ProductType
        fields = ['id', 'title', 'parent', 'children', 'created_at', 'updated_at']

    def get_children(self, obj):
        children = ProductType.objects.filter(parent=obj)
        serializer = ProductTypeSerializer(children, many=True)
        return serializer.data

class DriverPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPayment
        fields = '__all__'
class MerchantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantPayment
        fields = '__all__'