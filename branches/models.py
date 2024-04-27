from django.db import models



class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=55, null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    email = models.CharField(max_length=55, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'branches'


class PickupZone(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_id =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'pickup_zones'



class DeliveryZone(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch_id =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = 'delivery_zone'
