from riders.models import Rider
from riders.serializers import RidersSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class RiderList(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]

    
class RiderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]
