# Generated by Django 4.1 on 2022-11-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_card_is_active'),
        ('messages_my', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='id_card',
            field=models.ManyToManyField(to='ads.card', verbose_name='Товар'),
        ),
    ]
