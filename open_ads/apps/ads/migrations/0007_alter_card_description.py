# Generated by Django 4.1 on 2022-11-18 09:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_card_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]