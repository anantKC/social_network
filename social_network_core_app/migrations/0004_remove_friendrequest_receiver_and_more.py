# Generated by Django 4.1.7 on 2023-03-04 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_core_app', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='sender',
        ),
        migrations.DeleteModel(
            name='FriendList',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
