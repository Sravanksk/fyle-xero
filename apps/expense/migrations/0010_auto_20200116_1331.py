# Generated by Django 2.2.8 on 2020-01-16 13:31

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_auto_20200116_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensegroup',
            name='description',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='Description'),
        ),
    ]