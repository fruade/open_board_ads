from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from apps.ads.filters import CardFilter
from apps.ads.models import Card


class FavoritesView(FilterView):
    model = Card
    filterset_class = CardFilter
    template_name = 'favorites/favorite-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cards_favorites = self.request.session.get('favorites', None)
        if cards_favorites:
            cards_favorites = [i.get('type', None) for i in cards_favorites]
            context['card'] = Card.objects.filter(slug__in=cards_favorites)
            paginator = Paginator(context['card'], 10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['page_obj'] = page_obj
        else:
            paginator = None
        return context


def add_to_favorites(request):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

    item_exist = next((item for item in request.session['favorites'] if item['type'] == request.POST.get('type') and
                       item['id'] == request.POST.get('id')), False)

    add_data = {
        'type': request.POST.get('type'),
        'id': request.POST.get('id')
    }

    if not item_exist:
        request.session['favorites'].append(add_data)
        request.session.modified = True

        if request.accepts('text/html'):
            data = {
                'type': request.POST.get('type'),
                'id': request.POST.get('id')
            }
            request.session.modified = True
            return JsonResponse(data)
    return redirect(request.POST.get('url_from'))


def remove_from_favorites(request):
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item['id'] == request.POST.get('id') and item['type'] == request.POST.get('type'):
                item.clear()

        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        if not request.session['favorites']:
            del request.session['favorites']

    if request.accepts('text/html'):
        data = {
            'type': request.POST.get('type'),
            'id': request.POST.get('id')
        }
        request.session.modified = True
        return JsonResponse(data)
    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    if request.get('favorites'):
        del request.session['favorites']
    return redirect(request.POST.get('url_from'))


def favorites_api(request):
    return JsonResponse(request.session.get('favorites'), safe=False)