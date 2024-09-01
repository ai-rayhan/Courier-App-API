from datetime import datetime
from accounts.models import MerchantPayment,RiderPayment
from decimal import Decimal
from parcels.models import Parcel
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from parcels.models import StatusTracking
from admin_settings.models import DeliveryStatus
from riders.models import Rider
from rest_framework.response import Response

class MakeMerchantPayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_id = request.data.get('merchant_id')
        parcel_ids = request.data.get('parcels_id')
        status_id = request.data.get('status')
        payment = request.data.get('payment')
        payment_to = request.data.get('payment_to')
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
            payment_to_id=payment_to,
            note=note,
            total_payment=Decimal(payment),
            total_parcel_amount=total_parcel_amount,
            total_cod=total_cod,
            total_charge=total_charge,
            created_by=f"{request.user.username} ({request.user.role.name})"
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
            parcel.driver_payment_status = 1
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
            total_delivery_charge=total_charge,
            created_by=f"{request.user.username} ({request.user.role.name})"
        )

        return Response('Updated successfully', status=200)
