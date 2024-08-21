from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
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
from webcourier.permissions import HasSpecificPermission,IsSiteAdmin,IsSuperUser
from merchants.models import Merchant
from riders.models import Rider
from receiver.models import Receiver
from merchants.serializers import MerchantSerializer
from riders.serializers import RidersSerializer
############################# Authentication Section ######################

class SignUp(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            password = user_serializer.validated_data['password']
            hashed_password = make_password(password)
            user_serializer.validated_data['password'] = hashed_password

            user = user_serializer.save()
            user_type = request.data.get('user_type')

            if user_type == 'merchant':
                merchant_data = request.data.get('merchant', {})
                merchant_data['user'] = user.id
                merchant_serializer = MerchantSerializer(data=merchant_data)
                if merchant_serializer.is_valid():
                    merchant_serializer.save()
                    return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    # Delete the user if merchant creation fails
                    user.delete()
                    return Response(merchant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            elif user_type == 'rider':
                rider_data = request.data.get('rider', {})
                rider_data['user'] = user.id
                rider_serializer = RidersSerializer(data=rider_data)
                if rider_serializer.is_valid():
                    rider_serializer.save()
                    return Response(user_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    # Delete the user if rider creation fails
                    user.delete()
                    return Response(rider_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                # Handle unknown user type
                user.delete()
                return Response({"error": "Unknown user type"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignIn(APIView):
    def post(self, request):
     email = request.data.get('email')
     password = request.data.get('password')
     
     user = authenticate(username=email, password=password)
     
     if user is not None:
         if user.is_active:
             refresh = RefreshToken.for_user(user)
             return Response({
                 'status': True,
                 'message': 'Success',
                 'data': {
                     'refresh': str(refresh),
                     'access': str(refresh.access_token),
                     'id':user.id,
                     'email': user.email,
                     'name': user.username,
                     'phone': user.phone_number,
                     'role': user.role.id if user.role else None,
                     'merchant_id': Merchant.objects.filter(user_id=user.id).first().id if Merchant.objects.filter(user_id=user.id).exists() else None,
                     'rider_id': Rider.objects.filter(user_id=user.id).first().id if Rider.objects.filter(user_id=user.id).exists() else None,
                     'receiver_id': Receiver.objects.filter(user_id=user.id).first().id if Receiver.objects.filter(user_id=user.id).exists() else None,
                     'full_name': user.full_name,
                     'address': user.address,
                     'photo_url': user.photo.url if user.photo else None,
                     'is_phone_verified': user.is_phone_verified,
                     'is_active': user.is_active,
                 }
             })
         else:
             return Response({
                 'status': False,
                 'message': 'Account is inactive'
             }, status=status.HTTP_403_FORBIDDEN)
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
    
from django.http import JsonResponse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
def get_permissions(request):
    permissions = Permission.objects.all().select_related('content_type')

    permission_data = []
    for permission in permissions:
        permission_data.append({
            'id': permission.id,
            'codename': permission.codename,
            'content_type_app_label': permission.content_type.app_label,
            'content_type_model': permission.content_type.model,
        })
    sorted_permission_data = sorted(permission_data, key=lambda x: x['id'])

    # Remove the first 25 elements
    filtered_permission_data = sorted_permission_data[24:]
    return JsonResponse({'permissions': filtered_permission_data})
################################# OTP Section ###############################################

# class SendOTP(APIView):
#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         user = User.objects.filter(phone_number=phone_number).first()
        
#         if not user:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         # Generate OTP
#         otp = random.randint(100000, 999999)
#         otp_str = str(otp)

#         response = OTPSender.send_otp(phone_number, otp_str+" Don't share it another")
#         print(response.text)
#         if response.status_code == 200:
#             json_response = response.json()
#             response_code = json_response.get("response_code")
#             error_message = json_response.get("error_message")

#             if response_code == 202:
#                 # Save OTP to database
#                 OTP.objects.create(user=user, otp=str(otp))
#                 return Response({"message": "OTP sent successfully."}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Failed to send OTP", "details": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response({"error": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class VerifyOTPAndChangePassword(APIView):
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

class VerifyOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_provided = request.data.get('otp')

        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        otp_record = OTP.objects.filter(user=user).order_by('-timestamp').first()
        if otp_record and otp_record.is_valid() and otp_record.otp == otp_provided:
            user.is_phone_verified=True
            user.save()
            otp_record.delete()  # Clear OTP after use
            return Response({"message": "Phone Verification successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)

##################################### User permissions ###############################
class DeactivatedUser(APIView):
    def post(self, request):
        is_active = request.data.get('is_active')
        user_id = request.data.get('id')
        role = request.data.get('role')

        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        else:
            user.is_active=is_active
            user.role=role
            user.save()
            return Response({"message": "Request handle Sucessfully"}, status=status.HTTP_200_OK)

####################################### Role Section  #################################
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer    
    # permission_classes = [IsAuthenticated,HasSpecificPermission]
    # permission_codenames = ['view_role', 'change_role']
    def create(self, request, *args, **kwargs):
        permissions_data = request.data.pop('permissions', []) 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role = serializer.save()

        # Assign permissions to the role
        role.permissions.set(permissions_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated,HasSpecificPermission]
    permission_codename = ['change_role']
    def update(self, request, *args, **kwargs):
        permissions_data = request.data.pop('permissions', []) 
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        role = serializer.save()

        # Update permissions for the role
        role.permissions.set(permissions_data)

        return Response(serializer.data)



  
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


import random
from django.shortcuts import get_object_or_404
from admin_settings.models import SmsProvider
from users.models import OTP, User
from users.sms_providers import BulkSMSSMSProvider, TwilioSMSProvider, get_sms_provider_credentials



class SendOTP(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = get_object_or_404(User, phone_number=phone_number)

        # Generate OTP
        otp = random.randint(100000, 999999)
        otp_str = str(otp)

        # Choose SMS provider
        provider_name = request.data.get('provider', 'twilio')
        credentials = get_sms_provider_credentials(provider_name)

        if not credentials:
            return Response({"error": "Invalid SMS provider."}, status=status.HTTP_400_BAD_REQUEST)

        if provider_name == 'twilio':
            sms_provider = TwilioSMSProvider(
                account_sid=credentials['account_sid'],
                auth_token=credentials['auth_token'],
                from_number=credentials['from_number']
            )
        elif provider_name == 'bulksms':
            sms_provider = BulkSMSSMSProvider(
                api_key=credentials['api_key'],
                sender_id=credentials['sender_id']
            )
        else:
            return Response({"error": "Invalid SMS provider."}, status=status.HTTP_400_BAD_REQUEST)

        # Send OTP via chosen provider
        message = f"Your OTP is {otp_str}. Don't share it with anyone."
        response = sms_provider.send_sms(phone_number, message)
        response_status = response.get('status', None)
        status_code = response.get('status_code', None)

        if status_code in [200, 201, 202, 204] or response_status in ['queued', 'sent', 'delivered', 'success']:
            # Save OTP to the database
            OTP.objects.create(user=user, otp=otp_str)
            return Response({"message": "OTP sent successfully.", "details": response}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to send OTP", "details": response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
