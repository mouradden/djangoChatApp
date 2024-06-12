# Generated by Django 5.0.6 on 2024-06-12 12:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_chat_receiver_alter_chat_sender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mychats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.JSONField(default=dict)),
                ('frnd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_frnd', to=settings.AUTH_USER_MODEL)),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_me', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='chat',
        ),
    ]
