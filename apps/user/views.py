from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from apps.categories.models import Category
from allauth.account.views import SignupView, LoginView


class MySignupView(SignupView):
    template_name = 'my_signup.html'


class MyLoginView(LoginView):
    template_name = 'my_login.html'


