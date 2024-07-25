from parcels.models import Parcel
from parcels.serializers import ParcelSerializer,RiderParcelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from parcels.permissions import CanUpdateParcelPermission
from rest_framework import mixins
from rest_framework import generics

from parcels.models import StatusTracking
class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save()
class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated,CanUpdateParcelPermission]

class RiderParcelUpdate(generics.UpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = RiderParcelSerializer
    permission_classes = [IsAuthenticated]

####### Custom view #######
from rest_framework import status
from rest_framework.response import Response

class UpdateParcelStatus(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
       
        
        # Attempt to update the Parcel status
        try:
            serializer.save(delivery_status_id=request.data.get('delivery_status_id'))
        except:
            return Response({"error": "Failed to update Parcel status"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the Parcel status was successfully updated
        if instance.delivery_status_id == int(request.data.get('delivery_status_id')):
            # Status updated successfully, create StatusTracking object
            StatusTracking.objects.create(
                parcel_id=instance.id,
                status_id=instance.delivery_status.id,
                created_by=request.user.username+"("+request.user.role.name+")" # Assuming you're using authentication
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to update Parcel status"}, status=status.HTTP_400_BAD_REQUEST)
