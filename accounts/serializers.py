from rest_framework import serializers
from .models import MoneyReceipt,Ledger

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'
class MoneyReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyReceipt
        fields = '__all__'
