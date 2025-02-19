from django.db import migrations

def create_initial_branch(apps, schema_editor):
    Branch = apps.get_model('branches', 'Branch')
    Branch.objects.create(name='Default', phone='012345678910', email='Branch@gmail.com', address='Default')

def create_initial_pickupzone(apps, schema_editor):
    PickupZone = apps.get_model('branches', 'PickupZone')
    Branch = apps.get_model('branches', 'Branch')
    branch = Branch.objects.get(name='Default')
    PickupZone.objects.create(name='Default', branch_id=branch)

def create_initial_deliveryzone(apps, schema_editor):
    DeliveryZone = apps.get_model('branches', 'DeliveryZone')
    Branch = apps.get_model('branches', 'Branch')
    branch = Branch.objects.get(name='Default')
    DeliveryZone.objects.create(name='Default', branch_id=branch)
    
class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_branch),
        migrations.RunPython(create_initial_pickupzone),
        migrations.RunPython(create_initial_deliveryzone),
    ]
