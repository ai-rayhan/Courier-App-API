from rest_framework import serializers
from .models import Branch,PickupZone,DeliveryZone

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
class PickupZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupZone
        fields = '__all__'
class DeliveryZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryZone
        fields = '__all__'