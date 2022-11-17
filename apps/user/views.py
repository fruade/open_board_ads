from allauth.account import app_settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf, request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView
from django_filters.views import FilterView
from apps.user.forms import MyUpdateUserForm
from apps.ads.models import Card
from apps.categories.models import Category
from allauth.account.views import (
    SignupView, LoginView, PasswordResetView, PasswordResetFromKeyView, PasswordResetDoneView,
    PasswordResetFromKeyDoneView, EmailVerificationSentView, ConfirmEmailView, PasswordChangeView
)

from apps.user.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    model = User
    form_class = MyUpdateUserForm
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(level=0)
        context['card'] = Card.objects.all()
        context['title'] = 'Профиль'
        return context


class MySignupView(SignupView):
    template_name = 'user/signup.html'


class MyLoginView(LoginView):
    template_name = 'user/login.html'


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/password_change.html'
    success_url = reverse_lazy("account_change_password_done")


class MyPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/password_change_done.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset_done.html'


class MyPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'user/password_reset_from_key.html'


class MyPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = 'user/password_reset_from_key_done.html'


class MyEmailVerificationSentView(EmailVerificationSentView):
    template_name = 'user/verification_sent.html'


class MyConfirmEmailView(ConfirmEmailView):
    template_name = 'user/email_confirm.html'

