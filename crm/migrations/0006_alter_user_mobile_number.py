# Generated by Django 5.0.1 on 2024-02-23 06:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Mobile_Number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
