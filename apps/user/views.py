from allauth.account import app_settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from apps.categories.models import Category
from allauth.account.views import (
    SignupView, LoginView, PasswordResetView, PasswordResetFromKeyView, PasswordResetDoneView,
    PasswordResetFromKeyDoneView, EmailVerificationSentView, ConfirmEmailView
)


class MySignupView(SignupView):
    template_name = 'user/signup.html'


class MyLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = '/'


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

