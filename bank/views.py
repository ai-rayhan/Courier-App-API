from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Method,Information
from .serializers import MathodSerializer,InformationSerializer
from webcourier.utility.custom_response import custom_response  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_payment_mathod(request):
    if request.method == 'POST':
        # if str(request.user.id)=='admin tpye id':
            # return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
        serializer = MathodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_payment_mathod(request, pk):
    try:
        merchant = Method.objects.get(pk=pk)
    except Method.DoesNotExist:
        return custom_response(data="Not found.",status=status.HTTP_404_NOT_FOUND)
    # if str(request.data.get('user')) != str(request.user.id):
    #     return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)

    if request.method == 'PUT':
        serializer = MathodSerializer(merchant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



##########################################################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bank_information(request):
    if request.method == 'POST':
        # if str(request.user.id)=='admin tpye id':
            # return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_bank_information(request, pk):
    try:
        info = Information.objects.get(pk=pk)
    except Information.DoesNotExist:
        return custom_response(data="Not found.",status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = InformationSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data)
        return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class InformationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_info = Information.objects.filter(user=request.user)
        serializer = InformationSerializer(user_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = InformationSerializer(data=data, many=True)
        if serializer.is_valid():
            for item in serializer.validated_data:
                # item['user'] = request.user
                item.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        updated_info = []
        errors = []
        
        for item in data:
            info_id = item.get('id')
            try:
                info_instance = Information.objects.get(id=info_id, user=request.user)
            except Information.DoesNotExist:
                errors.append(f"Information with id {info_id} not found.")
                continue
            
            serializer = InformationSerializer(info_instance, data=item, partial=True)
            if serializer.is_valid():
                serializer.save()
                updated_info.append(serializer.data)
            else:
                errors.append(serializer.errors)
        
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(updated_info, status=status.HTTP_200_OK)