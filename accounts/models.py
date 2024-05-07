from django.db import models


class Ledger(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant= models.ForeignKey("merchants.Merchant", on_delete=models.CASCADE)
    date = models.DateField()
    voucher_id = models.CharField(max_length=255)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.ForeignKey("bank.Method", on_delete=models.CASCADE,null=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2)
    total_charge = models.DecimalField(max_digits=8, decimal_places=2,)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'ledgers'



class MoneyReceipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    ledger= models.ForeignKey(Ledger, on_delete=models.CASCADE)
    voucher_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'money_receipts'


class RiderPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    rider = models.ForeignKey("riders.Rider", on_delete=models.CASCADE)
    date = models.DateField()
    total_parcel = models.IntegerField()
    voucher_id = models.TextField(max_length=255)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.ForeignKey("bank.Method", on_delete=models.CASCADE)
    # method_payment = models.TextField(null=True, blank=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_cod = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_delivery_charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_commission = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'riders_payments'



class MerchantPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey("merchants.Merchant", on_delete=models.CASCADE)
    date = models.DateField()
    total_parcel = models.IntegerField()
    voucher_id = models.CharField(max_length=255,)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.ForeignKey("bank.Method", on_delete=models.CASCADE,null=True)
    # method_payment = models.TextField(null=True, blank=True)
    payment_info = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=8, decimal_places=2)
    total_charge = models.DecimalField(max_digits=8, decimal_places=2)
    total_cod = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_parcel_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'merchant_payments'
