# from rest_framework import permissions

# class CanUpdateRolePermission(permissions.BasePermission):
#     """
#     Custom permission to check if the user can update a Role object.
#     """

    # def has_permission(self, request, view):
    #     # Check if the user has the specific permission added to their role
    #     if request.user.role:
    #         return request.user.role.permissions.filter(codename='change_role').exists()
    #     return False


from rest_framework import permissions

class HasSpecificPermission(permissions.BasePermission):
    """
    Custom permission to check if the user has a specific permission.
    """

    def has_permission(self, request, view):
        # Check if the user has the specified permission codename
        permission_codename = getattr(view, 'permission_codename', None)
        if not permission_codename:
            return False  # No permission codename provided, deny access
        return request.user.has_specific_perm(permission_codename)



class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
