# Generated by Django 3.2.1 on 2021-05-26 18:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulator_groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=30000)),
                ('domain', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('alias', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('color', models.CharField(default='#08a2dc', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='simulator_images')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='simulator_logos')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='simulator_favicons')),
                ('owner_generated_domain', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('admin_comment_request_price', models.PositiveIntegerField(default=10)),
                ('order_lesson', models.BooleanField(default=False)),
                ('onboarding_skip', models.BooleanField(blank=True, default=False, null=True)),
                ('onboarding_name', models.CharField(blank=True, default='Онбординг', max_length=200, null=True)),
                ('simulator_script', models.TextField(blank=True, null=True)),
                ('sequence_no', models.PositiveIntegerField()),
                ('css', models.FileField(default='simulator_css/default.css', upload_to='simulator_css', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['css'])])),
                ('token', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('notifications_url', models.CharField(blank=True, max_length=300, null=True)),
                ('agreement_url', models.CharField(blank=True, max_length=300, null=True)),
                ('data_processing_url', models.CharField(blank=True, max_length=300, null=True)),
                ('completed_by_user_set', models.ManyToManyField(blank=True, related_name='completed_simulators', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simulator_groups.simulatorgroup')),
            ],
        ),
        migrations.CreateModel(
            name='SimulatorSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_message_text', models.TextField(blank=True, null=True)),
                ('welcome_message_author_name', models.CharField(blank=True, max_length=255, null=True)),
                ('welcome_message_author_img', models.ImageField(blank=True, null=True, upload_to='simulator_images')),
                ('main_color', models.CharField(blank=True, max_length=255, null=True)),
                ('message_after_task', models.TextField(blank=True, null=True)),
                ('pay_TerminalKey', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_EmailCompany', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_password', models.CharField(blank=True, max_length=255, null=True)),
                ('message_after_chapter', models.TextField(blank=True, null=True)),
                ('text_button_after_chapter', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram', models.CharField(blank=True, max_length=300, null=True)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('vkontakte', models.CharField(blank=True, max_length=300, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=300, null=True)),
                ('simulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulators.simulator')),
            ],
        ),
    ]
