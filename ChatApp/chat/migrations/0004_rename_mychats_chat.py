# Generated by Django 5.0.6 on 2024-06-11 17:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_chats_mychats_content_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mychats',
            new_name='chat',
        ),
    ]
