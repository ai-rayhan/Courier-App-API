from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_initial_roles(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    Role.objects.bulk_create([
        Role(name='Super Admin'),
        Role(name='Admin'),
        Role(name='Merchant'),
        Role(name='Rider'),
        Role(name='Receiver'),
        Role(name='General'),
    ])

def add_permissions_to_all_roles(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    Permission = apps.get_model('auth', 'Permission')

    # Get all roles
    roles = Role.objects.all()

    # Get all permissions
    permissions = Permission.objects.all()

    # Assign all permissions to all roles
    for role in roles:
        role.permissions.set(permissions)
        role.save()

def create_initial_user(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Role = apps.get_model('users', 'Role')

    # Retrieve roles
    super_admin_role = Role.objects.get(name='Super Admin')
    rider_role = Role.objects.get(name='Rider')
    merchant_role = Role.objects.get(name='Merchant')

    # Create users in bulk
    users = [
        User(
            email='superadmin@gmail.com',
            username='Super Admin',
            password=make_password('123456'),
            phone_number='012345678910',
            role=super_admin_role,
            is_superuser=True,
            is_admin=True,
            is_staff=True,
            is_phone_verified=True,
        ),
        User(
            email='rider@gmail.com',
            username='Rider',
            password=make_password('riderpassword'),
            phone_number='098765432109',
            role=rider_role,
            is_superuser=False,
            is_admin=False,
            is_staff=True,
            is_phone_verified=True,
        ),
        User(
            email='merchant@gmail.com',
            username='Merchant',
            password=make_password('merchantpassword'),
            phone_number='012345678901',
            role=merchant_role,
            is_superuser=False,
            is_admin=False,
            is_staff=True,
            is_phone_verified=True,
        ),
    ]
    
    User.objects.bulk_create(users)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),  # Ensure this matches your actual migration dependency
    ]

    operations = [
        migrations.RunPython(create_initial_roles),
        migrations.RunPython(add_permissions_to_all_roles),
        migrations.RunPython(create_initial_user),
    ]
