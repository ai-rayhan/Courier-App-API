# serializers.py
from rest_framework import serializers
from .models import Merchant,Shops

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['merchant_name','bussiness_contact_info','bussiness_address',
                #   'is_approved','is_active'
                  ]

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
  