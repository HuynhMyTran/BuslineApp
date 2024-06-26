# Generated by Django 4.2.13 on 2024-05-15 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buslines', '0006_alter_buses_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='buslines.customer'),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='buslines.driver'),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='buslines.driver'),
        ),
    ]
