# Generated by Django 4.1.7 on 2023-03-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_core_app', '0014_rename_last_name_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
