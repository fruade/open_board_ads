from django.db import models
from django.urls import reverse
from slugify import slugify
from ckeditor.fields import RichTextField
from apps.user.models import User
from apps.categories.utils import upload_images
from apps.categories.models import Category
from apps.ads.validators import max_file_size
from random import randint


class Card(models.Model):
    CHOICES_CONDITION = (
        ('Новое', 'Новое'),
        ('Б\у', 'Б\у')
    )

    title = models.CharField(max_length=25, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    id_category = models.ForeignKey(Category,
                                    on_delete=models.CASCADE,
                                    related_name='category_card',
                                    verbose_name='Категория',
                                    default=None
                                    )
    id_user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='user_card',
                                verbose_name='Пользователь',
                                default=None
                                )
    condition = models.CharField(max_length=50,
                                 verbose_name='Состояние',
                                 choices=CHOICES_CONDITION,
                                 default=CHOICES_CONDITION[0][0]
                                 )
    description = RichTextField(verbose_name='Описание')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_active = models.BooleanField(default=False, verbose_name='Архив')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    def get_absolute_url(self):
        return reverse('card', kwargs={'category': self.id_category.slug, 'slug': self.slug})

    class Meta:
        unique_together = [['id_user', 'slug']]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-date_add']

    def __str__(self):
        return self.slug


class CardPhoto(models.Model):
    card_img = models.ImageField(upload_to=upload_images,
                                 verbose_name='Фотографии', blank=True, null=True, validators=[max_file_size])
    id_card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='photos')

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.id_card.slug}"


