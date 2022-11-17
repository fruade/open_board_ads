from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from slugify import slugify
from random import randint
from apps.ads.filters import CardFilter
from apps.ads.forms import CardProductForm, CardProductUpdateForm
from apps.ads.models import Card, CardPhoto


class CardProductCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardProductForm
    template_name = 'ads/card_product_create.html'
    success_url = reverse_lazy('my_card_product')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        card_slug = str(self.object.slug) + str(randint(1, 1000000))
        self.object.slug = slugify(card_slug)
        self.object.id_user = self.request.user
        self.object.save()
        for key in form.files:
            img_files = form.files.getlist(key)
            if img_files:
                for file in img_files:
                    CardPhoto.objects.create(card_img=file, id_card=self.object)
            else:
                raise ValidationError("Загрузите минимум 1 фото")

        return super().form_valid(form)


class CardProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = 'ads/card_product_delete.html'
    success_url = reverse_lazy('my_card_product')


class CardProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardProductUpdateForm
    template_name = 'ads/card_product_update.html'
    success_url = reverse_lazy('my_card_product')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = self.object.slug
        self.object.id_user = self.request.user
        self.object.photos.all().delete()
        self.object.save()
        for key in form.files:
            img_files = form.files.getlist(key)
            if img_files:
                for file in img_files:
                    CardPhoto.objects.create(card_img=file, id_card=self.object)
            else:
                raise ValidationError("Загрузите минимум 1 фото")

        return super().form_valid(form)


class MyCardProductView(TemplateView):
    model = Card
    filterset_class = CardFilter
    template_name = 'ads/my_product_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context['card'] = Card.objects.filter(id_user=user_id)
        paginator = Paginator(context['card'], 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context


class CardProductView(DetailView):
    model = Card
    template_name = 'ads/card_product_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        phone_object = str(self.object.id_user.phone_number)
        phone = "{}{}-{}{}{}-{}{}{}-{}{}-{}{}".format(*phone_object)
        context['phone'] = str(phone)

        return context