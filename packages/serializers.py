from rest_framework import serializers
from packages.models import Packages

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'