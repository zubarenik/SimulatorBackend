# Generated by Django 3.2.3 on 2021-08-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('simulators', '0006_auto_20210815_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('default_role', models.CharField(max_length=200)),
                ('is_user', models.BooleanField(default=False)),
                ('male', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='character_avatars')),
                ('simulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulators.simulator')),
            ],
        ),
    ]
