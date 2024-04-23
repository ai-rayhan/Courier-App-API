from django.db import models
from merchants.models import*
class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    receiver = models.IntegerField()
    pickup_driver_id = models.IntegerField(null=True, blank=True)
    driver_id = models.IntegerField(null=True, blank=True)
    return_driver_id = models.IntegerField(null=True, blank=True)
    delivery_status = models.SmallIntegerField()
    voucher_id = models.CharField(max_length=30)
    pickup_zone_id = models.IntegerField(null=True, blank=True)
    delivery_zone_id = models.IntegerField(null=True, blank=True)
    date = models.DateField()
 
    cash_collection = models.DecimalField(max_digits=8, decimal_places=2)
    partial_cash_collection = models.FloatField(null=True, blank=True)
    cod = models.FloatField(null=True, blank=True)
    parcel_equivalent_price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2)
    payment = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    merchant_invoice_id = models.CharField(max_length=25, null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)

    pickup_address = models.TextField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_address = models.TextField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    issue_id = models.IntegerField(null=True, blank=True)
    issue_note = models.TextField(null=True, blank=True)
    payment_status = models.SmallIntegerField(default=1)
    driver_payment_status = models.SmallIntegerField(default=1)
    payment_date = models.DateField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'packages'

    def __str__(self):
        return self.voucher_id
