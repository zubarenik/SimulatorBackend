# Generated by Django 3.2.3 on 2021-08-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20210815_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlessonprogress',
            name='start_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]