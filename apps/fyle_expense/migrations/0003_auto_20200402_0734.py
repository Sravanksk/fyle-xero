# Generated by Django 2.2.8 on 2020-04-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyle_expense', '0002_auto_20200319_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(blank=True, help_text='Fyle Expense Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_id',
            field=models.CharField(help_text='Expense ID', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_number',
            field=models.CharField(help_text='Expense Number', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='project',
            field=models.CharField(blank=True, help_text='Project', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='purpose',
            field=models.TextField(blank=True, help_text='Purpose', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='report_id',
            field=models.CharField(help_text='Report ID', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='settlement_id',
            field=models.CharField(help_text='Settlement ID', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='state',
            field=models.CharField(help_text='Expense state', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='sub_category',
            field=models.CharField(blank=True, help_text='Fyle Expense Sub-Category', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='vendor',
            field=models.CharField(blank=True, help_text='Vendor', max_length=255, null=True),
        ),
    ]
