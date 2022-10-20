from apps.user.forms import MySignupForm
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordKeyForm


def get_context_data(request):
    context = {
        # 'login': LoginForm(),
        # 'signup': MySignupForm(),
        # 'reset_password': ResetPasswordKeyForm()
    }
    return context
