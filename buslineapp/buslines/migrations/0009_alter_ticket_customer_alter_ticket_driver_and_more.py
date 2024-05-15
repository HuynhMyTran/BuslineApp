# Generated by Django 4.2.13 on 2024-05-15 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buslines', '0008_user_description_alter_sellerprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to='buslines.customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='driver', to='buslines.driver'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seller', to='buslines.seller'),
        ),
    ]