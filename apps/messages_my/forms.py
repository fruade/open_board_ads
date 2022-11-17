from django import forms
from django.forms import ModelForm
from apps.messages_my.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}