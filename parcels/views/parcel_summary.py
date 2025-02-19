# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from parcels.models import Parcel
from merchants.models import Merchant
from parcels.serializers import ParcelSummarySerializer
from django.db.models import Sum, Count, F, Q
from django.shortcuts import get_object_or_404

class MerchantParcelSummaryView(APIView):
    def get(self, request, merchant_id, *args, **kwargs):
        # merchant = get_object_or_404(Merchant, id=merchant_id)

        summary = Parcel.objects.filter(merchant=merchant_id).aggregate(
            total_parcel=Count('id'),
            approved=Count('id', filter=Q(delivery_status=2)),  # Assuming 1 means approved
            delivery=Count('id', filter=Q(delivery_status=8)),  # Assuming 2 means delivered
            partial=Count('id', filter=Q(delivery_status=7)),  # Assuming 3 means partial
            return_returned=Count('id', filter=Q(delivery_status__in=[9, 10])),  # Assuming 4 means return and 5 means returned
            parcel_price=Sum('parcel_equivalent_price'),
            cash_collection=Sum('cash_collection'),
            merchant_paid=Sum('payment'),
            delivery_charge=Sum('delivery_charge')
        )

        serializer = ParcelSummarySerializer(summary)
        return Response(serializer.data)

class RiderParcelSummaryView(APIView):
    def get(self, request, rider_id, *args, **kwargs):
        summary = Parcel.objects.filter( Q(driver_id=rider_id) | Q(pickup_driver_id=rider_id)).aggregate(
            total_parcel=Count('id'),
            approved=Count('id', filter=Q(delivery_status=2)),
            assigned=Count('id', filter=Q(delivery_status=3)),  # Assuming 1 means approved
            delivery=Count('id', filter=Q(delivery_status=8)),  # Assuming 2 means delivered
            partial=Count('id', filter=Q(delivery_status=7)),  # Assuming 3 means partial
            return_returned=Count('id', filter=Q(delivery_status__in=[9, 10])),  # Assuming 4 means return and 5 means returned
            parcel_price=Sum('parcel_equivalent_price'),
            cash_collection=Sum('cash_collection'),
            merchant_paid=Sum('payment'),
            delivery_charge=Sum('delivery_charge')
        )

        serializer = ParcelSummarySerializer(summary)
        return Response(serializer.data)
