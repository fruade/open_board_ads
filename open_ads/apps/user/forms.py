from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import exceptions, validators
from django.utils.translation import gettext_lazy as _, gettext, pgettext
from allauth.account.forms import LoginForm, SignupForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from apps.user.models import User


class MySignupForm(SignupForm):
    phone_number = PhoneNumberField(
        region='RU',
        widget=PhoneNumberPrefixWidget(initial='RU'),
    )
    username = forms.CharField(max_length=16)
    city = forms.CharField()

    def save(self, request):
        user = super(MySignupForm, self).save(request)
        user.phone_number = self.cleaned_data["phone_number"]
        user.city = self.cleaned_data['city']
        user.save()
        return user


class MyUpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number', 'city',)



