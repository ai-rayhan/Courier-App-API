from parcels.models import Parcel
from parcels.serializers import ParcelSerializer,RiderParcelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from parcels.permissions import CanUpdateParcelPermission
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from parcels.models import StatusTracking
from django.db import models

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
from merchants.models import Merchant
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
                models.Q(pickup_driver_id=rider_id) |
                models.Q(driver_id=rider_id) |
                models.Q(return_driver_id=rider_id)
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

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

    # "merchent_id": selectedParcels.first.merchant,
    # "payment_method": ['1'],
    # "payment": ["$amount"],
    # "parcels_id": ["${selectedParcels.first.id}"],
    # "update_status_id": 13,
    # "payment_note": ["Payment Made By Admin"],
    # "note": "Monthly settlement"
from datetime import datetime
from accounts.models import MerchantPayment,RiderPayment
from decimal import Decimal

class MakeMerchantPayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_id = request.data.get('merchant_id')
        parcel_ids = request.data.get('parcels_id')
        status_id = request.data.get('status')
        payment = request.data.get('payment')
        payment_method = request.data.get('payment_method')
        payment_note = request.data.get('payment_note')
        note = request.data.get('note')

        if not isinstance(parcel_ids, list) or not isinstance(status_id, int):
            return Response('Invalid data', status=400)

        # Fetch the DeliveryStatus instance
        delivery_status = DeliveryStatus.objects.filter(id=status_id).first()
        if not delivery_status:
            return Response('Invalid status ID', status=400)
    
        # Initialize totals as Decimal
        total_parcel_amount = Decimal(0.0)
        total_cod = Decimal(0.0)
        total_charge = Decimal(0.0)
        
        parcels = Parcel.objects.filter(id__in=parcel_ids)
        if not parcels.exists():
            return Response('No parcels found', status=404)

        for parcel in parcels:
            if parcel.driver_payment_status==1:
              parcel.delivery_status = delivery_status
            parcel.payment_status = 1
            parcel.payment_date = datetime.now()
            print('Parcel updated')
            parcel.save()
            
            # Ensure all additions are with Decimal types
            total_parcel_amount += parcel.parcel_equivalent_price
            total_cod += parcel.cod
            total_charge += parcel.delivery_charge
            print('Parcel saved')
            StatusTracking.objects.create(
                parcel_id=parcel.id,
                status_id=delivery_status.id,
                created_by=f"{request.user.username} ({request.user.role.name})"
            )
        
        MerchantPayment.objects.create(
            merchant_id=merchant_id,
            date=datetime.now().date(),
            total_parcel=len(parcels),
            payment_info=payment_note,
            payment_method_id=payment_method,
            note=note,
            total_payment=Decimal(payment),
            total_parcel_amount=total_parcel_amount,
            total_cod=total_cod,
            total_charge=total_charge
        )

        return Response('Updated successfully', status=200)
    


class MakeRiderPayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        drider_id = request.data.get('drider_id')
        parcel_ids = request.data.get('parcels_id')
        status_id = request.data.get('status')
        payment = request.data.get('payment')
        payment_method = request.data.get('payment_method')
        payment_note = request.data.get('payment_note')

        if not isinstance(parcel_ids, list) or not isinstance(status_id, int) or not isinstance(payment, (str, int, float)):
            return Response('Invalid data', status=400)

        # Fetch the DeliveryStatus instance
        delivery_status = DeliveryStatus.objects.filter(id=status_id).first()
        if not delivery_status:
            return Response('Invalid status ID', status=400)

        parcels = Parcel.objects.filter(id__in=parcel_ids)
        if not parcels.exists():
            return Response('No parcels found', status=404)

        # Fetch the Rider instance
        rider = Rider.objects.filter(id=drider_id).first()
        rider_commission = rider.rider_commission if rider.rider_commission is not None else 0
        if not rider:
            return Response('Rider not found', status=404)

        # Initialize totals as Decimal
        total_commission = Decimal(0.0)
        total_cod = Decimal(0.0)
        total_charge = Decimal(0.0)

        for parcel in parcels:
            if parcel.payment_status==1:
              parcel.delivery_status = delivery_status
            parcel.payment_status = 1
            parcel.payment_date = datetime.now()
            parcel.save()

            # Ensure all additions are with Decimal types
            total_commission += (Decimal(rider_commission) / 100) * Decimal(parcel.cod)
            total_cod += Decimal(parcel.cod)
            total_charge += Decimal(parcel.delivery_charge)

            StatusTracking.objects.create(
                parcel_id=parcel.id,
                status_id=delivery_status.id,
                created_by=f"{request.user.username} ({request.user.role.name})"
            )

        RiderPayment.objects.create(
            rider_id=drider_id,
            date=datetime.now().date(),
            total_parcel=len(parcels),
            payment_info=payment_note,
            payment_method_id=payment_method,
            total_payment=Decimal(payment),
            total_commission=total_commission,
            total_cod=total_cod,
            total_delivery_charge=total_charge
        )

        return Response('Updated successfully', status=200)
