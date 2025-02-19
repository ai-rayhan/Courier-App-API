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
    serializer_class = DeliveryZoneSerializer
    def get_queryset(self):
        branch_id = self.request.query_params.get('branch_id')
        queryset = DeliveryZone.objects.all()  

        if branch_id is not None:
            try:
                branch_id = int(branch_id) 
                queryset = DeliveryZone.objects.filter(branch_id=branch_id)
            except ValueError:
                queryset = DeliveryZone.objects.all() 
        return queryset

    
class DeliveryZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryZone.objects.all()
    serializer_class = DeliveryZoneSerializer

class PickupZoneList(generics.ListCreateAPIView):
    serializer_class = PickupZoneSerializer

    def get_queryset(self):
        branch_id = self.request.query_params.get('branch_id')
        queryset = PickupZone.objects.all() 

        if branch_id is not None:
            try:
                branch_id = int(branch_id)
                queryset = PickupZone.objects.filter(branch_id=branch_id)
            except ValueError:
                queryset = PickupZone.objects.all()
        return queryset

class PickupZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickupZone.objects.all()
    serializer_class =PickupZoneSerializer
