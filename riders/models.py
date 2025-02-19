from django.db import models
from django.conf import settings
class Rider(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()
    vehicle_type = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    rider_commission = models.FloatField(null=True, blank=True)
    status=models.CharField(default='0',max_length=1,db_comment='0=inactive,1=active,2=soft delete')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.full_name
