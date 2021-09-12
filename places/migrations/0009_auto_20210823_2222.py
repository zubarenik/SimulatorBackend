# Generated by Django 3.2.3 on 2021-08-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20210823_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeuser',
            old_name='answer',
            new_name='answers',
        ),
        migrations.AddField(
            model_name='place',
            name='award_error',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='forced_role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='is_author_message',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='is_hero',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='is_multiple',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='postreply_error_female_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='postreply_error_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
