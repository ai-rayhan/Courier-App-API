from django.db import models
from django.core.exceptions import ValidationError
from django.db import models

def validate_image(image):
    # Ensure image has a 1:1 aspect ratio
    if image.width != image.height:
        raise ValidationError("Image must have a 1:1 aspect ratio.")
    
class DeliveryStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    image = models.ImageField(upload_to='delivery_status/', null=True, blank=True, validators=[validate_image])
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'delivery_statuses'



class StatusTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    parcel = models.ForeignKey("parcels.Parcel", on_delete=models.CASCADE)
    # date = models.DateField()
    status = models.ForeignKey(DeliveryStatus, on_delete=models.CASCADE)
    # status_mode = models.CharField(max_length=255)
    note = models.CharField(max_length=255, null=True, blank=True)
    # driver_id = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'status_trackings'
