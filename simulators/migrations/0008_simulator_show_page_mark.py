# Generated by Django 3.2.3 on 2021-09-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulators', '0007_simulatoruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulator',
            name='show_page_mark',
            field=models.BooleanField(default=True),
        ),
    ]