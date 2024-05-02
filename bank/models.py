from django.db import models
from django.conf import settings

class Method(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(Method, on_delete=models.CASCADE)  
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    updated_at = models.DateTimeField(auto_now=True,null=True)     
    def __str__(self):
        return f"{self.user}'s Information"

