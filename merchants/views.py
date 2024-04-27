from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Merchant,Shops
from .serializers import MerchantSerializer,ShopSerializer
from webcourier.utility.custom_response import custom_response  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_merchant(request):
    if request.method == 'POST':
        if Merchant.objects.filter(user=request.user).exists():
             return custom_response(error= 'A merchant already exists for this user', status=status.HTTP_400_BAD_REQUEST,success=False)
        if str(request.data.get('user')) != str(request.user.id):
            return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_merchant(request, pk):
    try:
        merchant = Merchant.objects.get(pk=pk)
    except Merchant.DoesNotExist:
        return custom_response(error="Not found.",status=status.HTTP_404_NOT_FOUND,success=False)

    if request.method == 'PUT':
        serializer = MerchantSerializer(merchant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########################################################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_shop(request):
    if request.method == 'POST':
        # Check if the user ID in the request data matches the authenticated user's ID
        if str(request.data.get('user')) != str(request.user.id):
            return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_shop(request, pk):
    try:
        shop = Shops.objects.get(pk=pk)
    except Shops.DoesNotExist:
        return custom_response(data="Not found.",status=status.HTTP_404_NOT_FOUND)

    # Check if the user ID in the request data matches the authenticated user's ID
    if str(request.data.get('user')) != str(request.user.id):
        return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)

    if request.method == 'PUT':
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework import generics
from packages.models import Parcel
from packages.serializers import ParcelSerializer

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