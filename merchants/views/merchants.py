from rest_framework import status,generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from merchants.models import Merchant,Shops
from merchants.serializers import MerchantSerializer,ShopSerializer
from webcourier.utility.custom_response import custom_response  
from merchants.permissions import IsActiveMerchantPermission  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_merchant(request):
    if request.method == 'POST':
        if Merchant.objects.filter(user=request.user).exists():
             return custom_response(error= 'A merchant already exists for this user', status=status.HTTP_400_BAD_REQUEST,success=False)
        # if str(request.data.get('user')) != str(request.user.id):
        #     return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_merchant(request):
    if request.method == 'GET':
        try:
            merchant = Merchant.objects.get(user=request.user)
            serializer = MerchantSerializer(merchant)
            return custom_response(serializer.data, status=status.HTTP_200_OK)
        except Merchant.DoesNotExist:
            return custom_response(data={'error': 'Merchant does not exist for this user'}, status=status.HTTP_404_NOT_FOUND)


        # Your existing create_merchant logic here

    
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

class MerchantList(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]
    
#########################################################

class ShopList(generics.ListCreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method  in ['POST']:
            return [IsAuthenticated()]  
        return super().get_permissions() 
    
class UpdateShop(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class =ShopSerializer
    permission_classes = [IsAuthenticated]

    

class ShopByMerchant(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id

        queryset = Shops.objects.filter(user_id=user_id)
        
        return queryset


