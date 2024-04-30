from rest_framework import permissions

class CanUpdateParcelPermission(permissions.BasePermission):
    """
    Custom permission to allow updating parcel if delivery status is smaller than 5.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the delivery status of the parcel is greater than 5
        if obj.delivery_status_id < 1:
            # print("Delivery Status Id:"+ obj.delivery_status_id)
            return True
        return False