from apps.user.forms import MySignupForm
from allauth.account.forms import LoginForm, SignupForm


def get_context_data(request):
    context = {
        'login': LoginForm(),
        'signup': MySignupForm(),
    }
    return context
