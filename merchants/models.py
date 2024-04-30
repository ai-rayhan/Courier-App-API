from django.db import models
from django.conf import settings 

class Merchant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=True)
    merchant_name = models.CharField(max_length=100)
    bussiness_contact_info = models.CharField(max_length=100)
    bussiness_address = models.CharField(max_length=100)
    soft_delete=models.BooleanField(default=False,blank=True,null=True)
    is_reviewed=models.BooleanField(default=False,blank=True,null=True)
    is_active=models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.merchant_name
    class Meta:
       db_table = 'merchants'
    

class Shops(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    merchant=models.ForeignKey(Merchant, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    shop_email = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    pickup_zone = models.CharField(max_length=100)
    pickup_phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.shop_name
