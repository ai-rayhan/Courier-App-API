# serializers.py
from rest_framework import serializers
from .models import Method,Information

class MathodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'
