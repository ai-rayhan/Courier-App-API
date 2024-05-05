from django.db import models
from webcourier.utility.small_image_validator import validate_image

class DeliveryTimes(models.Model):
    id = models.BigAutoField(primary_key=True)
    time_slot = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'delivery_times'


#Reference: https://chat.openai.com/share/3e1d43fe-5337-4f44-bedf-8c3422f2b7cb
class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'product_types'

    def __str__(self):
        return self.title


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

