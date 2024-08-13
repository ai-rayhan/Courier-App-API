from riders.models import Rider
from riders.serializers import RidersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from bank.serializers import BankInformationSerializer
from bank.models import BankInformation
from users.serializers import UserSerializer
from users.models import User

class RiderList(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]
class UpdateRider(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]

class RiderDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, rider_id):
        try:
            rider = Rider.objects.get(id=rider_id)
            rider_data = RidersSerializer(rider).data
            
            user = rider.user
            user_data = UserSerializer(user).data

            information = BankInformation.objects.filter(user=rider.user)
            information_data = BankInformationSerializer(information, many=True).data
            
            rider_data['userdetails'] = user_data
            rider_data['bank_information'] = information_data
            
            return Response(rider_data)
        
        except Rider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RiderActivate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        rider_ids = request.data.get('riders_id')
        status = request.data.get('status')

        if not isinstance(rider_ids, list) or not isinstance(status, int):
            return Response('Invalid data', status=400)

        updated_merchants= Rider.objects.filter(id__in=rider_ids).update(status=status)

        if updated_merchants:
            user_ids = Rider.objects.filter(id__in=rider_ids).values_list('user_id', flat=True)
            User.objects.filter(id__in=user_ids).update(role=4)
            
        return Response('Updated successfully')