from rest_framework import serializers
from .models import Parcel,Issue,ParcelDetails,ReturnParcel

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
class ParcelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelDetails
        fields = '__all__'
class ReturnParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnParcel
        fields = '__all__'