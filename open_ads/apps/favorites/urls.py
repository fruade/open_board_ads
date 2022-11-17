from django.urls import path
from apps.favorites.views import FavoritesView, add_to_favorites, remove_from_favorites, delete_favorites, favorites_api


urlpatterns = [
    path('', FavoritesView.as_view(), name='favorites_list'),
    path('add/', add_to_favorites, name='add_to_favorites'),
    path('remove/', remove_from_favorites, name='remove_from_favorites'),
    path('delete/', delete_favorites, name='delete_favorites'),
    path('api/', favorites_api, name='favorites_api')
]