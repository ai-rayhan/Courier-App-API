from rest_framework import serializers
from .models import DeliveryTimes,ProductType,DeliveryStatus

class DeliveryTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTimes
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ProductType
        fields = ['id', 'title', 'parent', 'children', 'created_at', 'updated_at']
        
    def get_children(self, obj):
        children_queryset = obj.children.all()
        children_serializer = self.__class__(children_queryset, many=True)
        return children_serializer.data

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'