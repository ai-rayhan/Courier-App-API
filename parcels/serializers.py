from rest_framework import serializers
from .models import Parcel,Issue,ParcelDetails,ReturnParcel,StatusTracking
from datetime import datetime

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        
        # Generate the voucher_id
        today_date = datetime.today().strftime('%Y%m%d')
        today_parcels_count = Parcel.objects.filter(voucher_id__startswith=f'NE-{today_date}').count()
        unique_id = today_parcels_count + 1
        validated_data['voucher_id'] = f'NE-{today_date}{unique_id}'
        
        return Parcel.objects.create(**validated_data)

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