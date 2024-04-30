
from rest_framework import generics
from parcels.models import Parcel
from parcels.serializers import ParcelSerializer
from rest_framework.permissions import IsAuthenticated

class PackageList(generics.ListCreateAPIView):
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        merchant_id = self.request.user.id
        delivery_status_id = self.request.query_params.get('delivery_status')

        # If delivery_status_id is provided in query params, filter by it
        if delivery_status_id is not None:
            queryset = Parcel.objects.filter(merchant_id=merchant_id, delivery_status_id=delivery_status_id)
        else:
            queryset = Parcel.objects.filter(merchant_id=merchant_id)
        
        return queryset

# from rest_framework import generics
# from packages.models import Packages
# from packages.serializers import PackageSerializer

# class FilteredPackageList(generics.ListCreateAPIView):
#     serializer_class = PackageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Get the URL parameters
#         merchant_id = self.request.user.id
#         delivery_status_id = self.kwargs.get('delivery_status')

#         # Filter queryset based on URL parameters
#         queryset = Packages.objects.filter(merchant_id=merchant_id, delivery_status_id=delivery_status_id)
        
#         return queryset

# class PackageList(generics.ListCreateAPIView):
#     serializer_class = PackageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         merchant_id = self.request.user.id

#         queryset = Packages.objects.filter(merchant_id=merchant_id)
        
#         return queryset