# Generated by Django 2.2.4 on 2019-09-19 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xero_workspace', '0004_xerocredential_file_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xerocredential',
            name='pem_file',
        ),
    ]