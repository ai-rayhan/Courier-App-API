from django.db import models
from merchants.models import Merchant
from receiver.models import Receiver
from riders.models import Rider
from branches.models import PickupZone,DeliveryZone
from delivery_status.models import DeliveryStatus

class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    pickup_driver = models.ForeignKey(Rider, on_delete=models.CASCADE,related_name='pickup_packages',null=True ,blank=True)
    driver= models.ForeignKey(Rider, on_delete=models.CASCADE,related_name='delivery_packages',null=True ,blank=True)
    return_driver = models.ForeignKey(Rider, on_delete=models.CASCADE,related_name='return_packages',null=True ,blank=True)
    delivery_status = models.ForeignKey(DeliveryStatus, on_delete=models.CASCADE,default=1)
    pickup_zone = models.ForeignKey(PickupZone, on_delete=models.CASCADE)
    delivery_zone = models.ForeignKey(DeliveryZone, on_delete=models.CASCADE)
    issue = models.IntegerField(null=True, blank=True)
    payment_status = models.SmallIntegerField(default=1,help_text='0=pending and 1=payment')
    driver_payment_status = models.SmallIntegerField(default=1,help_text='0=pending and 1=payment')
   
    voucher_id = models.CharField(max_length=30)
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_address = models.TextField()
    pickup_address = models.TextField(null=True, blank=True)
    date = models.DateField()

    cash_collection = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    partial_cash_collection = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    cod = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    parcel_equivalent_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    merchant_invoice_id = models.CharField(max_length=25, null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    issue_note = models.TextField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'packages'

    def __str__(self):
        return self.voucher_id



class Issue(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'issues'
