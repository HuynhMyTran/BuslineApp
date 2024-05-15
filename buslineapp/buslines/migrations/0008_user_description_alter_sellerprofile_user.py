# Generated by Django 4.2.13 on 2024-05-15 09:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buslines', '0007_alter_customerprofile_user_alter_driverprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sellerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='buslines.seller'),
        ),
    ]