from rest_framework import serializers
from .models import MoneyReceipt,Ledger,DriverPayment,MerchantPayment

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'
class MoneyReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyReceipt
        fields = '__all__'

class DriverPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPayment
        fields = '__all__'
class MerchantPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantPayment
        fields = '__all__'