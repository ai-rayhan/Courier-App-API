from django.urls import path
from .views import UserProfileView,UserProfileUpdate,SendOTP,VerifyOTPAndChangePassword,VerifyOTP,RoleList,RoleDetail,ActivateUserAndUpdateRole,SignIn,SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', SignIn.as_view(),name="signin"),
    path('viewprofile/', UserProfileView.as_view(), name='view_profile'),
    path('updateprofile/',UserProfileUpdate.as_view(), name='update_profile'),
    path('send-otp/', SendOTP.as_view(), name='send_otp'),
    path('verify-otp-password/', VerifyOTPAndChangePassword.as_view(), name='verify_otp_password'),
    path('verifyphone-otp/', VerifyOTP.as_view(), name='verify_otp'),
    path('activate-user/', ActivateUserAndUpdateRole.as_view(), name='activate-user'),
    # path('addrole/', add_role),
    # path('updaterole/<int:pk>/', update_role),
    # path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/', RoleList.as_view(), name='role-list'),
    path('roles/<int:pk>/', RoleDetail.as_view(), name='role-detail'),

]
