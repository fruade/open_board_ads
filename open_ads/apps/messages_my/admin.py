from django.contrib import admin

from apps.ads.models import CardPhoto
from apps.messages_my.models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'message', 'pub_date', 'is_read')
    list_display_links = ('id', 'chat', 'message',)


class MessageInline(admin.TabularInline):
    model = Message


class ChatAdmin(admin.ModelAdmin):
    inlines = [MessageInline, ]
    list_display = ('id', 'id_sender', 'id_recipient', 'id_card')
    list_display_links = ('id', 'id_sender', 'id_recipient', 'id_card')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)

