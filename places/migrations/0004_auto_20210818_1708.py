# Generated by Django 3.2.3 on 2021-08-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210802_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='node_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='node_position_x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='node_position_y',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
