# Generated by Django 2.2.8 on 2020-01-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyle_expense', '0003_expensegroup_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_number',
            field=models.CharField(help_text='Expense Number', max_length=64),
        ),
    ]
