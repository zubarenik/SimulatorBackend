# Generated by Django 3.2.3 on 2021-09-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20210906_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='correct_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]