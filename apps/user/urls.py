from allauth.account import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from apps.homepage.views import HomePageView
from apps.user.views import (
    MyLoginView, MySignupView, MyPasswordResetView, MyPasswordResetDoneView, MyPasswordResetFromKeyView,
    MyPasswordResetFromKeyDoneView, MyEmailVerificationSentView, MyConfirmEmailView
)


urlpatterns = [
    path("accounts/signup/", MySignupView.as_view(), name="account_signup"),
    path("accounts/login/", MyLoginView.as_view(), name="account_login"),
    path("accounts/password/reset/", MyPasswordResetView.as_view(), name="account_reset_password"),
    path("accounts/password/reset/done/", MyPasswordResetDoneView.as_view(), name="account_reset_password_done"),
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        MyPasswordResetFromKeyView.as_view(), name="account_reset_password_from_key",
    ),
    path(
        "accounts/password/reset/key/done/",
        MyPasswordResetFromKeyDoneView.as_view(), name="account_reset_password_from_key_done",
    ),
    path("accounts/confirm-email/", MyEmailVerificationSentView.as_view(), name="account_email_verification_sent"),
    re_path(
        r"^accounts/confirm-email/(?P<key>[-:\w]+)/$",
        MyConfirmEmailView.as_view(), name="account_confirm_email",
    ),
    # path(
    #     "password/change/",
    #     views.password_change,
    #     name="account_change_password",
    # ),
    # path("password/set/", views.password_set, name="account_set_password"),
    # path("inactive/", views.account_inactive, name="account_inactive"),
    # # E-mail
    # path("email/", views.email, name="account_email"),


]
