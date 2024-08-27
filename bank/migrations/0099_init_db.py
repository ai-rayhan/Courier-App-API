from django.db import migrations


def create_initial_payment_method(apps, schema_editor):

    PaymentMethod = apps.get_model('bank', 'PaymentMethod')

    PaymentMethod.objects.bulk_create([

        PaymentMethod(name='Online Payment'),

        PaymentMethod(name='Bank'),

        PaymentMethod(name='Cash'),

    ])

    

class Migration(migrations.Migration):


    dependencies = [

        ('bank', '0002_initial'),

    ]


    operations = [
        migrations.RunPython(create_initial_payment_method),
    ]

