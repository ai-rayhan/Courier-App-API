from admin_settings.models import ProductType
from admin_settings.serializers import ProductTypeSerializer
from rest_framework import generics
from webcourier.permissions import IsSuperUserORAdmin
from rest_framework.permissions import  IsAuthenticated

class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()

