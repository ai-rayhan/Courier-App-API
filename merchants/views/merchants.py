from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from merchants.models import Merchant,Shops
from merchants.serializers import MerchantSerializer,ShopSerializer
from webcourier.utility.custom_response import custom_response  
from merchants.permissions import IsActiveMerchantPermission  

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_merchant(request):
#     if request.method == 'POST':
#         if Merchant.objects.filter(user=request.user).exists():
#              return custom_response(error= 'A merchant already exists for this user', status=status.HTTP_400_BAD_REQUEST,success=False)
#         # if str(request.data.get('user')) != str(request.user.id):
#         #     return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
#         serializer = MerchantSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def get_merchant(request):
#     if request.method == 'GET':
#         try:
#             merchant = Merchant.objects.get(user=request.user)
#             serializer = MerchantSerializer(merchant)
#             return custom_response(serializer.data, status=status.HTTP_200_OK)
#         except Merchant.DoesNotExist:
#             return custom_response(data={'error': 'Merchant does not exist for this user'}, status=status.HTTP_404_NOT_FOUND)


#         # Your existing create_merchant logic here

    
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_merchant(request, pk):
#     try:
#         merchant = Merchant.objects.get(pk=pk)
#     except Merchant.DoesNotExist:
#         return custom_response(error="Not found.",status=status.HTTP_404_NOT_FOUND,success=False)

#     if request.method == 'PUT':
#         serializer = MerchantSerializer(merchant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return custom_response(data=serializer.data)
#         return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from bank.serializers import InformationSerializer
from bank.models import Information
from users.models import User
from users.serializers import UserSerializer

class Merchants(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]

class MerchantDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, merchant_id):
        try:
            merchant = Merchant.objects.get(id=merchant_id)
            merchant_data = MerchantSerializer(merchant).data
            
            user = merchant.user
            user_data = UserSerializer(user).data

            information = Information.objects.filter(user=merchant.user)
            information_data = InformationSerializer(information, many=True).data
            
            merchant_data['userdetails'] = user_data
            merchant_data['bank_information'] = information_data
            
            return Response(merchant_data)
        
        except Merchant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class MerchantActivate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_ids = request.data.get('merchant_ids')
        status = request.data.get('status')

        if not isinstance(merchant_ids, list) or not isinstance(status, int):
            return Response('Invalid data', status=400)

        updated_merchants= Merchant.objects.filter(id__in=merchant_ids).update(status=status)

        if updated_merchants:
            user_ids = Merchant.objects.filter(id__in=merchant_ids).values_list('user_id', flat=True)
            User.objects.filter(id__in=user_ids).update(role=3)

        return Response('Updated successfully')
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


