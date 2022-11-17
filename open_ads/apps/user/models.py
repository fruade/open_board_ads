from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True, region='RU', unique=False, default='Не заполнено',
                                    verbose_name='Номер телефона')
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    username = models.CharField(_("username"), max_length=150, unique=False, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

    def __str__(self):
        return self.email
