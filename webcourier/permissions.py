# Permission rules
# SuperUser:is_superuser+is_staff (backend)+roleid=1
# Admin:is_admin(backend)+roleid=2(Fronted Identifer)
# Merchant:role=3
# rider:role=4
# receiver:role=5
# default user receiver
from rest_framework import permissions


# from rest_framework import permissions

# class HasSpecificPermission(permissions.BasePermission):
#     """
#     Custom permission to check if the user has a specific permission.
#     """

#     def has_permission(self, request, view):
#         # Check if the user has the specified permission codename
#         permission_codename = getattr(view, 'permission_codename', None)
#         if not permission_codename:
#             return False  # No permission codename provided, deny access
#         return request.user.has_specific_perm(permission_codename)


class HasSpecificPermission(permissions.BasePermission):
    """
    Custom permission to check if the user has a specific permission.
    """

    def has_permission(self, request, view):
        # Check if the user has the required permission based on the HTTP method
        permission_codenames = getattr(view, 'permission_codenames', {})
        if request.method == 'GET' and 'view_role' in permission_codenames:
            return True
        elif request.method == 'POST' and 'add_role' in permission_codenames:
            return request.user.has_specific_perm('add_role')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_specific_perm('change_role')
        return False


class IsSiteAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser and request.user.is_staff)

class IsSuperUserORAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser or request.user.is_admin)



# class IsActiveMerchantPermission(permissions.BasePermission):
#     """
#     Custom permission to allow only active merchant.
#     """

#     def has_permission(self, request, view):
#         # Check if the user related to the merchant is active
#         if hasattr(request.user, 'merchant'):  # Assuming you have a one-to-one relationship between User and Merchant
#             return request.user.merchant.is_active
#         return False  # If the user doesn't have a related merchant or merchant is not active



# class HasSpecificPermission(permissions.BasePermission):
#     """
#     Custom permission to check if the user has a specific permission based on their role.
#     """

#     def __init__(self, permission_codename):
#         self.permission_codename = permission_codename

#     def has_permission(self, request, view):
#         # Check if the user has the specified permission codename
#         if not self.permission_codename:
#             return False  # No permission codename provided, deny access
        
#         # Check if the user has the permission based on their role
#         if request.user.has_perm(self.permission_codename):
#             return True
#         else:
#             return False

# class BranchList(generics.ListCreateAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             permission_codename = 'view_branch' 
#         else:
#             permission_codename = 'add_branch' 
        
#         return [HasSpecificPermission(permission_codename)]
