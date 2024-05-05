from rest_framework import serializers
from .models import Parcel,Issue,ParcelDetails,ReturnParcel,StatusTracking

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class RiderParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['pickup_driver','driver','return_driver','payment_status','driver_payment_status','cash_collection','partial_cash_collection','return_date','issue_note','payment_date','note']

class ParcelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelDetails
        fields = '__all__'

class StatusTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTracking
        fields = '__all__'
        
class ReturnParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnParcel
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'