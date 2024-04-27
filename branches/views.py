from .models import Branch,DeliveryZone,PickupZone
from .serializers import BranchSerializer,DeliveryZoneSerializer,PickupZoneSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]

    
class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]

class DeliveryZoneList(generics.ListCreateAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    permission_classes = [IsAuthenticated]

    
class DeliveryZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    permission_classes = [IsAuthenticated]

class PickupZoneList(generics.ListCreateAPIView):
    queryset = PickupZone.objects.all()
    serializer_class = PickupZoneSerializer
    permission_classes = [IsAuthenticated]

    
class PickupZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickupZone.objects.all()
    serializer_class =PickupZoneSerializer
    permission_classes = [IsAuthenticated]
