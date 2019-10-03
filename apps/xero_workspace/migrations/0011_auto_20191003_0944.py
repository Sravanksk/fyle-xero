# Generated by Django 2.2.4 on 2019-10-03 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xero_workspace', '0010_auto_20191003_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspaceactivity',
            name='activity',
            field=models.ForeignKey(blank=True, help_text='FK to Activity', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='sync_activity.Activity'),
        ),
    ]
