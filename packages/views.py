from packages.models import Packages
from packages.serializers import PackageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PackageList(generics.ListCreateAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

    
class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]
