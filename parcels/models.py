from django.db import models
from merchants.models import Merchant
from receiver.models import Receiver
from riders.models import Rider
from django.conf import settings 
from branches.models import PickupZone,DeliveryZone
from delivery_status.models import DeliveryStatus
from admin_settings.models import ProductType
from datetime import datetime

class Parcel(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
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
   
    voucher_id = models.CharField(max_length=30,blank=True)
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

    def save(self, *args, **kwargs):
        today_date = datetime.today().strftime('%Y%m%d')
        today_parcels_count = Parcel.objects.filter(voucher_id__startswith=f'NE-{today_date}').count()
        unique_id = today_parcels_count + 1
        self.voucher_id = f'NE-{today_date}{unique_id}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'parcel'

    def __str__(self):
        return self.voucher_id



class Issue(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'issues'



class ParcelDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    date = models.DateField()
    # client_id =  models.ForeignKey(Receiver, on_delete=models.CASCADE) ##Copy db field
    # merchant_id =  models.ForeignKey(Merchant, on_delete=models.CASCADE) ##Copy db field
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    item_description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height_left = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height_right = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'parcel_details'



class ReturnParcel(models.Model):
 
    id = models.BigAutoField(primary_key=True)
    parcel =  models.ForeignKey(Parcel, on_delete=models.CASCADE)
    merchant =  models.ForeignKey(Merchant, on_delete=models.CASCADE)
    receiver =  models.ForeignKey(Receiver, on_delete=models.CASCADE)
    driver =  models.ForeignKey(Rider, on_delete=models.CASCADE)
    return_status =  models.ForeignKey(DeliveryStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'parcel_returns'
