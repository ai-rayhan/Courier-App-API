from rest_framework import serializers
# from rest_framework.generics import RetrieveAPIView, UpdateAPIView
# from rest_framework.permissions import IsAuthenticated
from .models import User,Role

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','role']
        extra_kwargs = {'password': {'write_only': True}}


class ViewProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'photo', 'phone_number', 'address', 'role']
        read_only_fields = ['email', 'username']
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'photo', 'phone_number', 'address',]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

# class UserProfileView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserProfileSerializer

#     def get_object(self):
#         return self.request.user

# class UserProfileUpdate(UpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserProfileSerializer

#     def get_object(self):
#         return self.request.user

#     def get_queryset(self):
#         return User.objects.filter(pk=self.request.user.pk)

#     def perform_update(self, serializer):
#         serializer.save(email=self.request.user.email, username=self.request.user.username)
