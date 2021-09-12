# Generated by Django 3.2.1 on 2021-05-26 18:41

import certificates.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('simulators', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default=certificates.models.rand_slug, max_length=6, unique=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='certificates')),
                ('simulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulators.simulator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='certificate',
            index=models.Index(fields=['slug'], name='certificate_slug_1bb6ae_idx'),
        ),
    ]
