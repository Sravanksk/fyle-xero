# Generated by Django 2.2.8 on 2020-03-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xero_workspace', '0001_initial'),
        ('fyle_expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensegroup',
            name='invoice',
            field=models.ForeignKey(blank=True, help_text='FK to Invoice', null=True, on_delete=django.db.models.deletion.PROTECT, to='xero_workspace.Invoice'),
        ),
        migrations.AddField(
            model_name='expensegroup',
            name='workspace',
            field=models.ForeignKey(help_text='To which workspace this expense group belongs to', on_delete=django.db.models.deletion.CASCADE, to='xero_workspace.Workspace'),
        ),
        migrations.AddField(
            model_name='expense',
            name='invoice_line_item',
            field=models.ForeignKey(blank=True, help_text='FK to InvoiceLineItem', null=True, on_delete=django.db.models.deletion.PROTECT, to='xero_workspace.InvoiceLineItem'),
        ),
    ]
