from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.ads.models import Card
from apps.user.models import User


class Chat(models.Model):
    id_sender = models.IntegerField()
    id_recipient = models.IntegerField()
    id_card = models.ForeignKey(Card, verbose_name="Товар", on_delete=models.CASCADE)


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE, related_name='chat_message')
    message = models.TextField(verbose_name="Сообщение")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message

