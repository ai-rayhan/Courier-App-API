from django.db import models
from django.conf import settings 

class Merchant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=True)
    shop_name = models.CharField(max_length=100)
    pickup_phone = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    pickup_address = models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(default='0',max_length=1,db_comment='0=inactive,1=active,2=soft delete')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.merchant_name
    class Meta:
       db_table = 'merchants'
    

class Shops(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # merchant=models.ForeignKey(Merchant, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    shop_email = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    pickup_zone = models.ForeignKey("branches.PickupZone", on_delete=models.CASCADE,null=True,blank=True)
    pickup_phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.shop_name
