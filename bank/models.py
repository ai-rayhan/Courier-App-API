from django.db import models
from django.conf import settings

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'payment_method'

    def __str__(self):
        return self.name


    
class BankInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)  
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    updated_at = models.DateTimeField(auto_now=True,null=True)     

    class Meta:
        db_table = 'bank_info'

    def __str__(self):
        return f"{self.user}'s Information"

