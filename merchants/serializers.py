# serializers.py
from rest_framework import serializers
from .models import Merchant,Shops


class MerchantSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Get the context from serializer initialization
        context = kwargs.get('context', {})
        # If 'request' exists in context and 'user' is available in request
        if 'request' in context and context['request'].user:
            # Dynamically add 'user' field to the fields
            self.Meta.fields += ['user']

        super(MerchantSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Merchant
        fields = ['merchant_name', 'bussiness_contact_info', 'bussiness_address']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
  