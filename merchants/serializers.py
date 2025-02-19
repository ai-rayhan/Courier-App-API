# serializers.py
from rest_framework import serializers
from .models import Merchant,Shops

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
        read_only_fields = ['user']  

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)