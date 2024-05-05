from django.db import models

class Ledger(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_id = models.IntegerField(default=0)
    date = models.DateField()
    voucher_id = models.CharField(max_length=255, null=True, blank=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    method_payment = models.TextField(null=True, blank=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'ledgers'



class MoneyReceipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    ledger_id = models.IntegerField()
    voucher_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'money_receipts'


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
