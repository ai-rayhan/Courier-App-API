from django.db import models
from webcourier.utility.small_image_validator import validate_image

class DeliveryTimes(models.Model):
    id = models.BigAutoField(primary_key=True)
    delivery_type=models.CharField(max_length=255,blank=True)
    time_slot = models.CharField(max_length=255)
    estimated_days = models.CharField(max_length=255,blank=True)

    basic_charge=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    per_kg_weight = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    per_inch_height = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    per_inch_width = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    cash_collection_charge_percent = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'delivery_type_info'


#Reference: https://chat.openai.com/share/3e1d43fe-5337-4f44-bedf-8c3422f2b7cb
class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
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


class SmsProvider(models.Model):
    sms_provider = models.CharField(max_length=20, default='')
    account_sid = models.CharField(max_length=40, blank=True, null=True)
    auth_token = models.CharField(max_length=40, blank=True, null=True)
    from_number = models.CharField(max_length=20, blank=True, null=True)
    api_key = models.CharField(max_length=40, blank=True, null=True)
    sender_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'sms_provider'

        


class PaymentServiceProvider(models.Model):
    payment_service_provider = models.CharField(max_length=20, default='')
    account_sid = models.CharField(max_length=40, blank=True, null=True)
    auth_token = models.CharField(max_length=40, blank=True, null=True)
    from_number = models.CharField(max_length=20, blank=True, null=True)
    api_key = models.CharField(max_length=40, blank=True, null=True)
    sender_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'payment_service_provider'
