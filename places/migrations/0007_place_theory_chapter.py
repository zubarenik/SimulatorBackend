# Generated by Django 3.2.3 on 2021-08-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theories', '0002_alter_theorychapter_sequence_no'),
        ('places', '0006_alter_place_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='theory_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theories.theorychapter'),
        ),
    ]
