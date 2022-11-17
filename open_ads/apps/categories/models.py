from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Attributes(models.Model):
    attribute = models.CharField(max_length=50)


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
