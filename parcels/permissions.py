from rest_framework import permissions

class CanUpdateParcelPermission(permissions.BasePermission):
    """
    Custom permission to allow updating parcel if delivery status is smaller than 5.
    """

    def has_object_permission(self, request, view, obj):

        if request.user and (request.user.is_superuser or request.user.is_admin):
            return True
        
        if obj.delivery_status_id < 1:
            # print("Delivery Status Id:"+ obj.delivery_status_id)
            return True
        return False