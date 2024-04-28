from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ViewProfileSerializer,UpdateProfileSerializer,RoleSerializer
from .serializers import UserSerializer
from .models import Role,User,OTP
from webcourier.utility.custom_response import custom_response 
import os
import random
from webcourier.utility.otp_sender import OTPSender
from rest_framework import generics
from .permissions import HasSpecificPermission,IsAdmin,IsSuperUser

############################# Authentication Section ######################

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data['password']
        hashed_password = make_password(password) 
        serializer.validated_data['password'] = hashed_password 
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
       
    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': True,
            'message': 'Success',
            'data': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
             
            }
        })
    else:
        return Response({
            'status': False,
            'message': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)


############################# Profile Section ######################

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = ViewProfileSerializer(user)
        return Response(serializer.data)


class UserProfileUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            # Check if new file is being uploaded
            if 'photo' in request.FILES:
                # Delete the old file if it exists and is not the same as the new file
                old_file = user.photo
                if old_file and os.path.isfile(old_file.path):
                    # if not old_file == request.FILES['photo']:
                        os.remove(old_file.path)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################# OTP Section ###############################################

class SendOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Generate OTP
        otp = random.randint(100000, 999999)
        otp_str = str(otp)

        response = OTPSender.send_otp(phone_number, otp_str)
        print(response.text)
        if response.status_code == 200:
            json_response = response.json()
            response_code = json_response.get("response_code")
            error_message = json_response.get("error_message")

            if response_code == 202:
                # Save OTP to database
                OTP.objects.create(user=user, otp=str(otp))
                return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to send OTP", "details": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class VerifyOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_provided = request.data.get('otp')
        new_password = request.data.get('new_password')

        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        otp_record = OTP.objects.filter(user=user).order_by('-timestamp').first()
        if otp_record and otp_record.is_valid() and otp_record.otp == otp_provided:
            user.set_password(new_password)
            user.save()
            otp_record.delete()  # Clear OTP after use
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)


####################################### Role Section  #################################
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer    
    permission_classes = [IsAuthenticated, HasSpecificPermission,IsAdmin,IsSuperUser]
    permission_codename = 'change_role'

    
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated,HasSpecificPermission,IsAdmin,IsSuperUser]
    permission_codename = 'change_role'




  
        # api_url = "http://bulksmsbd.net/api/smsapi"
        # api_key = 'ZwO6786JCSDjwbVR3TrB'  # Get API key from Django settings
        # senderid = '8809617617743'  # Get sender ID from Django settings

        # # Message format with placeholders for OTP
        # message = f"Your OTP is {otp_str}"

        # # Parameters for API request
        # params = {
        #     "api_key": api_key,
        #     "senderid": senderid,
        #     "number": phone_number,
        #     "message": message
        # }

        # response = requests.post(api_url, data=params)

# @api_view(['PUT'])
# def update_role(request, pk):
#     try:
#         merchant = Role.objects.get(pk=pk)
#     except Role.DoesNotExist:
#         return custom_response(data="Not found.",status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = RoleSerializer(merchant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return custom_response(data=serializer.data)
#         return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class RoleListView(generics.ListAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer


####################################### Otp verification Section #################################

# class SendOTP(APIView):
#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         user = User.objects.filter(phone_number=phone_number).first()
#         if not user:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         print(phone_number)
#         otp = random.randint(100000, 999999)
#         OTP.objects.create(user=user, otp=str(otp))

#         # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#         # message = client.messages.create(
#         #     body=f'Your OTP is {otp}',
#         #     from_=settings.TWILIO_PHONE_NUMBER,
#         #     to=phone_number
#         # )

#         return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)



# @api_view(['POST'])
# def add_role(request):
#     if request.method == 'POST':
#         # if str(request.user.id)=='admin tpye id':
#             # return custom_response(error="You are not authorized to perform this action.", status=status.HTTP_403_FORBIDDEN, success=False)
        
#         serializer = RoleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return custom_response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return custom_response(error=serializer.errors, status=status.HTTP_400_BAD_REQUEST, success=False)

