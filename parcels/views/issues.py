from parcels.models import Issue
from parcels.serializers import IssueSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from webcourier.permissions import IsSuperUserORAdmin,HasSpecificPermission


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions() 
    
class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()
