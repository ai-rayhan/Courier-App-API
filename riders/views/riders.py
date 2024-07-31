from riders.models import Rider
from riders.serializers import RidersSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class RiderList(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]

    
class RiderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RidersSerializer
    permission_classes = [IsAuthenticated]

from bank.serializers import InformationSerializer
from bank.models import Information
class RiderDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch all merchants
        riders = Rider.objects.all()

        # Prepare a list to hold the serialized data
        response_data = []

        # Iterate through each merchant and gather related information
        for rider in riders:
            rider_data = RidersSerializer(rider).data
            
            # Fetch related information for the merchant's user
            information = Information.objects.filter(user=rider.user)
            information_data = InformationSerializer(information, many=True).data
            
            # Add the information data to the merchant data
            rider_data['bank_information'] = information_data
            
            # Append to the response list
            response_data.append(rider_data)
        
        return Response(response_data)

class RiderStatusUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_ids = request.data.get('riders_id')
        status = request.data.get('status')

        if not isinstance(merchant_ids, list) or not isinstance(status, int):
            return Response('Invalid data', status=400)

        # Update status for all merchants in the list
        Rider.objects.filter(id__in=merchant_ids).update(status=status)
        
        return Response('Updated successfully')