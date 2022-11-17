from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView

from apps.ads.models import Card, CardPhoto
from apps.ads.filters import CardFilter
from apps.categories.models import Category
from apps.feedback.forms import FeedBackForm
from apps.user.forms import MySignupForm
from allauth.account.forms import LoginForm

from apps.user.models import User


class HomePageView(FilterView):
    paginate_by = 10
    model = Card
    template_name = 'homepage/homepage.html'
    context_object_name = 'slider_categories'
    filterset_class = CardFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categories_for_slider'] = Category.objects.filter(level=0)
        context['card'] = self.model.objects.all()
        context['title'] = 'Главная страница'
        return context

