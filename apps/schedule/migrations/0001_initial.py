# Generated by Django 2.2.4 on 2019-09-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_at', models.DateTimeField(help_text='Schedule start at')),
                ('enabled', models.BooleanField(default=False, help_text='Schedule enabled')),
                ('time_interval', models.IntegerField(help_text="Time interval between successive sync's in minutes")),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at')),
            ],
        ),
    ]
