# Generated by Django 4.2.13 on 2024-05-13 14:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buslines', '0003_buses_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buses',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
