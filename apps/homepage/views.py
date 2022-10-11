from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView, TemplateView

from apps.categories.models import Category
from apps.user.forms import MySignupForm
from allauth.account.forms import LoginForm


class HomePageView(TemplateView):
    model = Category
    template_name = 'homepage/homepage.html'
    context_object_name = 'slider_categories'

    # def get(self, request, *args, **kwargs):
    #     my_sign_up_form = MySignupForm(self.request.GET or None)
    #     login_form = LoginForm(self.request.GET or None)
    #     context = self.get_context_data(**kwargs)
    #     context['signup'] = my_sign_up_form
    #     context['login'] = login_form
    #     return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.filter(level=0)
        context['title'] = 'Главная страница'
        return context


