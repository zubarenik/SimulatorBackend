# Generated by Django 3.2.3 on 2021-09-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_placeuser_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='points_error',
            field=models.IntegerField(default=0),
        ),
    ]