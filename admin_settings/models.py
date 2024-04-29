from django.db import models

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


class DriverPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_id = models.IntegerField(default=0)
    date = models.DateField()
    total_parcel = models.IntegerField(null=True, blank=True)
    voucher_id = models.TextField(null=True, blank=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    method_payment = models.TextField(null=True, blank=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_cod = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_delivery_charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_commission = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'driver_payments'



class MerchantPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_id = models.IntegerField(default=0)
    date = models.DateField()
    total_parcel = models.IntegerField(null=True, blank=True)
    voucher_id = models.CharField(max_length=255, null=True, blank=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    method_payment = models.TextField(null=True, blank=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_cod = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_parcel_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'merchant_payments'
