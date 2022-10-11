from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from apps.homepage.views import HomePageView
# from apps.user.views import LoginView
from django.contrib.auth.urls import *
urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('', include('django.contrib.auth.urls'))
]
