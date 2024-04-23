# serializers.py
from rest_framework import serializers
from .models import Receiver

class ReciverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = '__all__'
