# Generated by Django 3.2.1 on 2021-05-26 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sequence_no', models.PositiveIntegerField()),
                ('is_onboarding', models.BooleanField(default=False)),
                ('is_test', models.BooleanField(default=False)),
                ('need_answers', models.PositiveIntegerField(blank=True, null=True)),
                ('is_page_after_test', models.BooleanField(default=False)),
                ('completed_by_user_set', models.ManyToManyField(blank=True, related_name='completed_pages', to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
                ('page_after_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
                ('simulator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simulators.simulator')),
            ],
        ),
        migrations.CreateModel(
            name='UserPageProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utility', models.PositiveIntegerField(blank=True, null=True)),
                ('fun', models.PositiveIntegerField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('is_test_passed', models.BooleanField(blank=True, null=True)),
                ('is_show', models.BooleanField(default=False)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]