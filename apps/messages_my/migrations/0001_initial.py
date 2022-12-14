# Generated by Django 4.1 on 2022-10-31 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=6)),
                ('recipient', models.CharField(max_length=6)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=512, verbose_name='Сообщение')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки сообщения')),
                ('dialog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialog', to='messages_my.dialog', verbose_name='Диалог')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sender', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
        ),
    ]
