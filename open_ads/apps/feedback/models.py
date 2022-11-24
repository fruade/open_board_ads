from django.db import models
from ckeditor.fields import RichTextField
from apps.user.models import User


class FeedBack(models.Model):
    name = models.CharField(max_length=16, verbose_name='Имя')
    email = models.CharField(max_length=55, verbose_name='Email')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user_feedback',
                             verbose_name='Пользователь',
                             default=None
                             )
    feedback = models.TextField(verbose_name='Отзыв')
