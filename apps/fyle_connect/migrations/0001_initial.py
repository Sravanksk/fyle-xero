# Generated by Django 2.2.4 on 2019-09-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FyleAuth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(default='https://app.fyle.in', help_text='Base URL of the fyle environment', max_length=300)),
                ('client_id', models.CharField(help_text='Client Id', max_length=256)),
                ('client_secret', models.CharField(help_text='Client Secret', max_length=256)),
                ('refresh_token', models.CharField(help_text='Refresh Token', max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at')),
            ],
        ),
    ]
