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
    
from django.db.models import Count

class ParcelSummarybyStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_role = user.role.id
        print(user_role)
        if user_role==1 or user_role==2:
            # User role is 1 or 2, return counts for all delivery statuses
            status_counts = DeliveryStatus.objects.annotate(parcel_count=Count('parcel')).values('id', 'status','image','parcel_count')
        else:
            user_id = request.user.id

            if user_id is not None:
                try:
                    user_id = int(user_id)
                except ValueError:
                    return Response({'error': 'Invalid user ID'}, status=400)

                # Filter parcels by user ID and annotate delivery status with count of related parcels
                status_counts = DeliveryStatus.objects.filter(parcel__user_id=user_id).annotate(parcel_count=Count('parcel')).values('id', 'status','image', 'parcel_count')
            else:
                return Response({'error': 'User ID is required for filtering'}, status=400)

        # Convert to a list of dictionaries
        status_summary = list(status_counts)

        return Response(status_summary)