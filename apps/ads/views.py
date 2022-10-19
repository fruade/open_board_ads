from django.shortcuts import render
from django.views.generic import TemplateView

from apps.categories.models import Category


class HomePageAdsView(TemplateView):
    # model = Category
    template_name = 'ads/show_ads.html'
    # context_object_name = 'slider_categories'
