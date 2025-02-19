from django.db import migrations


def create_initial_payment_method(apps, schema_editor):
    PaymentMethod = apps.get_model('bank', 'PaymentMethod')

    PaymentMethod.objects.bulk_create([
        PaymentMethod(name='Online Payment'),
        PaymentMethod(name='Bank'),
        PaymentMethod(name='Cash'),
    ])


def create_initial_bank_info(apps, schema_editor):
    User = apps.get_model('users', 'User')
    PaymentMethod = apps.get_model('bank', 'PaymentMethod')
    user = User.objects.get(email='merchant@gmail.com')
    payment_method = PaymentMethod.objects.get(name='Bank')
    BankInformation = apps.get_model('bank', 'BankInformation')

    BankInformation.objects.create(
    user=user,
    payment_method=payment_method,
    bank_name='Test Bank Ltd',
    account_number='1234567890',
    account_name='John Doe',
    branch='Main Branch',
)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0099_init_db'),  
        ('bank', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_payment_method),
        migrations.RunPython(create_initial_bank_info),
    ]

