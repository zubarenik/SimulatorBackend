# Generated by Django 3.2.3 on 2021-08-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theorychapter',
            name='sequence_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
