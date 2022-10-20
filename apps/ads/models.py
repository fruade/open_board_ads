from django.db import models


class CardProduct(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя автора')
