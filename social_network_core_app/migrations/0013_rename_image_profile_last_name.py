# Generated by Django 4.1.7 on 2023-03-05 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_core_app', '0012_remove_friends_friends_delete_friendrequest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='last_name',
        ),
    ]