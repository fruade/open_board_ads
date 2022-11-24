from apps.categories.models import Category
from apps.user.forms import MySignupForm
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordKeyForm


def get_context_data(request):
    context = {
        'categories_for_slider': Category.objects.filter(level=0),
        # 'signup': MySignupForm(),
        # 'reset_password': ResetPasswordKeyForm()
    }
    return context
