from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_initial_merchant(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Merchant = apps.get_model('merchants', 'Merchant')
    user = User.objects.get(email='merchant@gmail.com')

    Merchant.objects.create(
        user=user,
        shop_name="Guest Merchant's Shop",
        pickup_phone="012345678901",
        shop_address="123 Merchant St.",
        pickup_address="123 Merchant St.",
        status='1',  
    )

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0099_init_db'),  
        ('merchants', '0002_initial'), 
    ]

    operations = [
        migrations.RunPython(create_initial_merchant),
    ]
