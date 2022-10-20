from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from apps.homepage.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]

