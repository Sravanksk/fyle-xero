# Generated by Django 2.2.4 on 2019-10-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync_activity', '0002_auto_20190912_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='sync_db',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='transform_sql',
        ),
        migrations.AddField(
            model_name='activity',
            name='sync_db_file_id',
            field=models.CharField(blank=True, help_text='SQLite database file Id', max_length=32, null=True),
        ),
    ]