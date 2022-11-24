from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views.generic import CreateView, TemplateView
from apps.ads.models import Card
from apps.messages_my.forms import MessageForm
from apps.messages_my.models import Message, Chat


class MessagesView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messages_my/create_message.html'

    def get_success_url(self):
        url = str(self.request.META.get('HTTP_REFERER')).split('/')
        url = '/'.join(url[:-3]) + '/'
        return url

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_card = Card.objects.get(slug=self.kwargs['slug'])
        try:
            print(self.kwargs)
            chat = Chat.objects.get(Q(id_sender=self.kwargs['author_id']) &
                                    Q(id_recipient=self.kwargs['user_id']) &
                                    Q(id_card=id_card))
        except Chat.DoesNotExist:
            chat = None

        if not chat:
            chat = Chat.objects.create(
                id_sender=self.kwargs['author_id'],
                id_recipient=self.kwargs['user_id'],
                id_card=id_card
            )

        self.object.chat = chat
        self.object.save()
        return super().form_valid(form)


class DialogView(LoginRequiredMixin, TemplateView):
    model = Chat
    template_name = 'messages_my/dialogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dialogs'] = Chat.objects.filter(Q(id_sender=self.request.user.id) |
                                                 Q(id_recipient=self.request.user.id))
        return context


