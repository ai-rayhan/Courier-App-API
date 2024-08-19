from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from merchants.models import Merchant,Shops
from merchants.serializers import MerchantSerializer,ShopSerializer
from bank.serializers import BankInformationSerializer
from bank.models import BankInformation
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

            information = BankInformation.objects.filter(user=merchant.user)
            information_data = BankInformationSerializer(information, many=True).data
            
            merchant_data['userdetails'] = user_data
            merchant_data['bank_information'] = information_data
            
            return Response(merchant_data)
        
        except Merchant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class UpdateMerchant(generics.RetrieveUpdateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]

    
class MerchantActivate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
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


