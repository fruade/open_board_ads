# Generated by Django 4.1 on 2022-11-15 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=55, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(verbose_name='Отзыв и предложение'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=16, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.PositiveIntegerField(verbose_name='Рейтинг'),
        ),
    ]
