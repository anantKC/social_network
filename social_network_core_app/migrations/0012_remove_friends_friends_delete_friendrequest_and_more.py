# Generated by Django 4.1.7 on 2023-03-05 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_core_app', '0011_friends_friendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friends',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]