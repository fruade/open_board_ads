from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from apps.feedback.forms import FeedBackForm
from apps.feedback.models import FeedBack


class FeedBackView(FormView):
    form_class = FeedBackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('feedback_done')

    def form_valid(self, form):
        feed = FeedBack(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            rating=form.cleaned_data['rating'],
            feedback=form.cleaned_data['feedback'],
            user=self.request.user
        )
        feed.save()
        return super(FeedBackView, self).form_valid(form)


def done(request):
    return render(request, 'feedback/feedback_done.html')

