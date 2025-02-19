from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_initial_rider(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Rider = apps.get_model('riders', 'Rider')
    user = User.objects.get(email='rider@gmail.com')

    Rider.objects.create(
    user=user,
    full_name="Guest Rider",
    email="rider@gmail.com",
    phone="0123456789",
    address="123 Main Street",
    vehicle_type="Bike",
    registration_number="ABC-1234",
    rider_commission=10.0,
    status='1', 
)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0099_init_db'),  
        ('riders', '0002_initial'), 
    ]

    operations = [
        migrations.RunPython(create_initial_rider),
    ]
