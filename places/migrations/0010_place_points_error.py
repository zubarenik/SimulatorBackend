# Generated by Django 3.2.3 on 2021-08-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210823_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='points_error',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
