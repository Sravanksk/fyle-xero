# Generated by Django 2.2.4 on 2020-01-09 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xero_connect', '0001_initial'),
        ('xero_workspace', '0009_delete_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xerocredential',
            name='consumer_key',
        ),
        migrations.RemoveField(
            model_name='xerocredential',
            name='private_key',
        ),
        migrations.AddField(
            model_name='xerocredential',
            name='xero_auth',
            field=models.OneToOneField(default=0, help_text='FK to Xero Auth', on_delete=django.db.models.deletion.CASCADE, to='xero_connect.XeroAuth'),
            preserve_default=False,
        ),
    ]