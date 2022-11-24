from django.urls import path, re_path

from apps.messages_my.views import MessagesView, DialogView

urlpatterns = [
    path('<str:category>/card_product/<slug:slug>/chat/<int:author_id>-to-<int:user_id>/', MessagesView.as_view(), name='create_message'),
    path('my_messages/', DialogView.as_view(), name='my_messages')
]

