from rest_framework import permissions
class IsActiveMerchantPermission(permissions.BasePermission):
    """
    Custom permission to allow only active merchant.
    """

    def has_permission(self, request, view):
        # Check if the user related to the merchant is active
        if hasattr(request.user, 'merchant'):  # Assuming you have a one-to-one relationship between User and Merchant
            return request.user.merchant.is_active
        return False  # If the user doesn't have a related merchant or merchant is not active
