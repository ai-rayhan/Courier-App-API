from .models import Branch,DeliveryZone,PickupZone
from .serializers import BranchSerializer,DeliveryZoneSerializer,PickupZoneSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin,HasSpecificPermission

class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    def get_permissions(self):
        if self.request.method  in ['POST']:
            permission_codename = 'add_branch' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),
                    # HasSpecificPermission(permission_codename)
                    ]  
        return super().get_permissions()  
    
class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    def get_permissions(self):
        if self.request.method  in ['PUT','DELETE']:
            permission_codename = 'change_branch' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),
                    # HasSpecificPermission(permission_codename)
                    ]  
        return super().get_permissions()  

class DeliveryZoneList(generics.ListCreateAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    def get_permissions(self):
        if self.request.method  in ['POST']:
            permission_codename = 'add_deliveryzone' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),
                    # HasSpecificPermission(permission_codename)
                    ]  
        return super().get_permissions()  

    
class DeliveryZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer
    def get_permissions(self):
        if self.request.method  in ['PUT','DELETE']:
            permission_codename = 'change_deliveryzone' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),HasSpecificPermission(permission_codename)]  
        return super().get_permissions()  

class PickupZoneList(generics.ListCreateAPIView):
    queryset = PickupZone.objects.all()
    serializer_class = PickupZoneSerializer
    def get_permissions(self):
        if self.request.method  in ['POST']:
            permission_codename = 'add_pickupzone' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),
                    # HasSpecificPermission(permission_codename)
                    ]  
        return super().get_permissions()  
    
class PickupZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickupZone.objects.all()
    serializer_class =PickupZoneSerializer
    def get_permissions(self):
        if self.request.method  in ['PUT','DELETE']:
            permission_codename = 'change_pickupzone' 
            return [IsAuthenticated(), IsSuperUserORAdmin(),HasSpecificPermission(permission_codename)]  
        return super().get_permissions()  
