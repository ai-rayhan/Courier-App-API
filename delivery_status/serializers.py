from rest_framework import serializers
from delivery_status.models import DeliveryStatus,StatusTracking

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'

class StatusTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTracking
        fields = '__all__'