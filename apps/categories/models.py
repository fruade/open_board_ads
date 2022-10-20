from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from apps.user.models import User
from apps.categories.utils import upload_images


class Attributes(models.Model):
    attribute = models.CharField(max_length=50)


class Card(models.Model):
    CHOICES_CONDITION = (
        ('Новое', 'Новое'),
        ('Б\у', 'Б\у')
    )

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    id_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='category_card',
        verbose_name='Категория',
        default=None
    )
    id_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_card',
        verbose_name='Пользователь',
        default=None
    )
    condition = models.CharField(max_length=50, verbose_name='Состояние',
                                 choices=CHOICES_CONDITION, default=CHOICES_CONDITION[0][0])
    description = models.TextField(blank=True, verbose_name='Описание')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    class Meta:
        unique_together = [['id_user', 'slug']]
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.slug


class CardPhoto(models.Model):
    card_img = models.ImageField(upload_to=upload_images,
                                 verbose_name='Фотографии', blank=True, null=True)
    id_card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='photos')

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.id_card.slug}"


class Category(MPTTModel):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            db_index=True, related_name='children', verbose_name='Родительская категория')
    cat_img = models.ImageField(upload_to='categories/category_img/',
                                verbose_name='Фото категории', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        unique_together = [['title', 'parent', 'slug']]
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])

    def __str__(self):
        return self.title
