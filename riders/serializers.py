from rest_framework import serializers
from riders.models import Rider

class RidersSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Rider
        fields = '__all__'
