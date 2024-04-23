from receiver.models import Receiver
from receiver.serializers import ReciverSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.appdecorators import has_role

class ReciverList(generics.ListCreateAPIView):
    queryset = Receiver.objects.all()
    serializer_class = ReciverSerializer
    permission_classes = [IsAuthenticated]

    
class ReceverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receiver.objects.all()
    serializer_class = ReciverSerializer
    permission_classes = [IsAuthenticated]
