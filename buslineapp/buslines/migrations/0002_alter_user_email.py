# Generated by Django 4.2.13 on 2024-05-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buslines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
