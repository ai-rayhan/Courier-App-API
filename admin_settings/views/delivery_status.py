from admin_settings.models import DeliveryStatus
from admin_settings.serializers import DeliveryStatusSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from webcourier.permissions import IsSuperUserORAdmin
from rest_framework.permissions import  IsAuthenticated
from parcels.models import Parcel
from parcels.serializers import ParcelSerializer


class DeliveryStatusList(generics.ListCreateAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]  
        return super().get_permissions()  
    
class DeliveryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryStatus.objects.all()
    serializer_class = DeliveryStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthenticated(), IsSuperUserORAdmin()]
        return super().get_permissions()
    
from django.db.models import Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from riders.models import Rider
from parcels.models import DeliveryStatus

class ParcelSummarybyStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_role = user.role.id
        
        if user_role == 1 or user_role == 2:
            # User role is 1 or 2, return counts for all delivery statuses
            status_counts = DeliveryStatus.objects.annotate(parcel_count=Count('parcel')).values('id', 'status', 'image', 'parcel_count')
        else:
            user_id = request.user.id
            if user_role == 3:
                status_counts = DeliveryStatus.objects.filter(parcel__user_id=user_id).annotate(parcel_count=Count('parcel')).values('id', 'status', 'image', 'parcel_count')
            elif user_role == 4:
                rider = Rider.objects.filter(user_id=user_id).first()  
                if rider is None:
                    return Response({'error': 'Rider not found for the given user ID'}, status=400)
                rider_id = rider.id
                status_counts = DeliveryStatus.objects.filter(
                        Q(parcel__driver_id=rider_id) | Q(parcel__pickup_driver_id=rider_id)
                ).annotate(parcel_count=Count('parcel')).values('id', 'status', 'image', 'parcel_count')
            else:
                return Response({'error': 'Invalid user role'}, status=400)

        # Convert to a list of dictionaries
        status_summary = list(status_counts)

        return Response(status_summary)
