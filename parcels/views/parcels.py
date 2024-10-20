from parcels.models import Parcel
from parcels.serializers import ParcelSerializer,RiderParcelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from parcels.permissions import CanUpdateParcelPermission
from rest_framework import generics
from rest_framework.views import APIView
from parcels.models import StatusTracking
from django.db import models
from rest_framework.response import Response
from rest_framework import status
from parcels.serializers import ViewParcelSerializer
from admin_settings.models import DeliveryStatus
from riders.models import Rider
from merchants.models import Merchant

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
    

class GetParcels(APIView):
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        delivery_status_id = self.request.query_params.get('delivery_status')
        # rider_id = self.request.query_params.get('rider')

        # Fetch the merchant associated with the current user
        merchant = Merchant.objects.filter(user=user).first()
        merchant_id = merchant.id if merchant else None
        rider = Rider.objects.filter(user=user).first()
        rider_id = rider.id if rider else None

        queryset = Parcel.objects.all()
        if (user.role.id==1 or user.role.id==2) and delivery_status_id:
             queryset = queryset.filter(delivery_status_id=delivery_status_id)
        if user.role.id==3 and delivery_status_id and merchant_id:
            queryset = queryset.filter(delivery_status_id=delivery_status_id,merchant_id=merchant_id)
        
        if user.role.id==4 and delivery_status_id and rider_id:
               queryset = queryset.filter(
                (models.Q(pickup_driver_id=rider_id) |
                models.Q(driver_id=rider_id) |
                models.Q(return_driver_id=rider_id)) and
                models.Q(delivery_status_id=delivery_status_id)
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

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