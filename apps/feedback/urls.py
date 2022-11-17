from django.urls import path
from apps.feedback.views import done, FeedBackView


urlpatterns = [
    path('done', done, name='feedback_done'),
    path('', FeedBackView.as_view(), name='feedback'),
]