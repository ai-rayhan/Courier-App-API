from admin_settings.models import SmsProvider
from admin_settings.serializers import SMSProviderSerializer
from rest_framework import generics
from webcourier.permissions import IsSuperUserORAdmin
from rest_framework.permissions import  IsAuthenticated

class SmsProviderList(generics.ListCreateAPIView):
    queryset = SmsProvider.objects.all()
    serializer_class = SMSProviderSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 

class SmsProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmsProvider.objects.all()
    serializer_class = SMSProviderSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()

