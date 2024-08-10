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
class ParcelUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated,CanUpdateParcelPermission]

class RiderParcelUpdate(generics.UpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = RiderParcelSerializer
    permission_classes = [IsAuthenticated]

####### Custom view #######
# from rest_framework import status
# from rest_framework.response import Response

# class UpdateParcelStatus(mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Parcel.objects.all()
#     serializer_class = ParcelSerializer
#     permission_classes = [IsAuthenticated]

#     def put(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
       
        
#         # Attempt to update the Parcel status
#         try:
#             serializer.save(delivery_status_id=request.data.get('delivery_status_id'))
#         except:
#             return Response({"error": "Failed to update Parcel status"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Check if the Parcel status was successfully updated
#         if instance.delivery_status_id == int(request.data.get('delivery_status_id')):
#             # Status updated successfully, create StatusTracking object
#             StatusTracking.objects.create(
#                 parcel_id=instance.id,
#                 status_id=instance.delivery_status.id,
#                 created_by=request.user.username+"("+request.user.role.name+")" # Assuming you're using authentication
#             )
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Failed to update Parcel status"}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from admin_settings.models import DeliveryStatus
# class UpdateParcelStatus(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         parcel_ids = request.data.get('parcel_ids')
#         status_id = request.data.get('status')

#         if not isinstance(parcel_ids, list) or not isinstance(status_id, int):
#             return Response('Invalid data', status=400)

#         # Fetch the DeliveryStatus instance
#         delivery_status = DeliveryStatus.objects.filter(id=status_id).first()
#         if not delivery_status:
#             return Response('Invalid status ID', status=400)

#         # Update status for all parcels in the list
#         parcels = Parcel.objects.filter(id__in=parcel_ids)
#         for parcel in parcels:
#             parcel.delivery_status = delivery_status
#             parcel.save()  # Save the DeliveryStatus update to the database

#             # Create a StatusTracking entry for each updated parcel
#             StatusTracking.objects.create(
#                 parcel_id=parcel.id,
#                 status_id=delivery_status.id,
#                 created_by=f"{request.user.username} ({request.user.role.name})"
#             )

#         return Response('Updated successfully')
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parcels.serializers import ViewParcelSerializer

class ParcelDetailView(APIView):
    def get(self, request, id):
        try:
            parcel = Parcel.objects.select_related(
                'merchant', 'receiver', 'pickup_driver', 
                'driver', 'return_driver', 'delivery_status',
                'pickup_zone', 'delivery_zone'
            ).get(id=id)
            
            serializer = ViewParcelSerializer(parcel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Parcel.DoesNotExist:
            return Response({"error": "Parcel not found."}, status=status.HTTP_404_NOT_FOUND)

from admin_settings.models import DeliveryStatus
from riders.models import Rider

class UpdateParcelStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        parcel_ids = request.data.get('parcel_ids')
        status_id = request.data.get('status')
        pickup_rider = request.data.get('pickup_rider')
        delivery_rider = request.data.get('delivery_rider')
        partial_collection_amount = request.data.get('partial_collection_amount')
        reason = request.data.get('reason')
        delivery_amount = request.data.get('delivery_amount')

        if not isinstance(parcel_ids, list) or not isinstance(status_id, int):
            return Response('Invalid data', status=400)

        # Fetch the DeliveryStatus instance
        delivery_status = DeliveryStatus.objects.filter(id=status_id).first()
        if not delivery_status:
            return Response('Invalid status ID', status=400)
        pickup_rider = Rider.objects.filter(id=pickup_rider).first() if pickup_rider else None
        delivery_rider = Rider.objects.filter(id=delivery_rider).first() if delivery_rider else None
        # Update status for all parcels in the list
        parcels = Parcel.objects.filter(id__in=parcel_ids)
        for parcel in parcels:
            parcel.delivery_status = delivery_status
            
            # Update the optional fields if they are provided
            if pickup_rider is not None:
                parcel.pickup_driver = pickup_rider
            if delivery_rider is not None:
                parcel.driver = delivery_rider
            if partial_collection_amount is not None:
                parcel.partial_cash_collection = partial_collection_amount
            if reason is not None:
                parcel.issue_note = reason
            if delivery_amount is not None:
                parcel.delivery_charge = delivery_amount

            parcel.save()  # Save the updates to the database

            # Create a StatusTracking entry for each updated parcel
            StatusTracking.objects.create(
                parcel_id=parcel.id,
                status_id=delivery_status.id,
                created_by=f"{request.user.username} ({request.user.role.name})"
            )

        return Response('Updated successfully')

