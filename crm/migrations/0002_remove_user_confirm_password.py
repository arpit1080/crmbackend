# Generated by Django 5.0.1 on 2024-02-23 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Confirm_Password',
        ),
    ]
