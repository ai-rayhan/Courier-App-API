# serializers.py
from rest_framework import serializers
from .models import PaymentMethod,BankInformation

class PaymentMathodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class BankInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = '__all__'
