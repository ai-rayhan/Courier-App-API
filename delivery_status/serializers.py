from rest_framework import serializers
from delivery_status.models import DeliveryStatus

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'