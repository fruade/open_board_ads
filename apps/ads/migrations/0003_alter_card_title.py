# Generated by Django 4.1 on 2022-10-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_card_cardphoto_delete_cardproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
    ]
