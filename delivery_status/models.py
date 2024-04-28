from django.db import models

class DeliveryStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True, blank=True)
    color_code = models.CharField(max_length=255, null=True, blank=True)
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'delivery_statuses'



class StatusTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking_id = models.PositiveIntegerField()
    date = models.DateField()
    status_id = models.PositiveSmallIntegerField(default=0)
    status_mode = models.CharField(max_length=255)
    note = models.CharField(max_length=255, null=True, blank=True)
    driver_id = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'status_trackings'
