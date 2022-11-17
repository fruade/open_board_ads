from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.ads.models import Card
from apps.user.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="Участник")
    id_card = models.ManyToManyField(Card, verbose_name="Товар")

    def get_absolute_url(self):
        return reverse('card', kwargs={'id_card': self.id_card.slug, 'chat_id': self.pk})


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message

