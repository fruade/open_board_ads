from django.urls import path
from apps.ads.views import CardProductCreateView, CardProductView, MyCardProductView, CardProductUpdateView, \
    CardProductDeleteView
from django_filters.views import FilterView


urlpatterns = [
    path('create_product/', CardProductCreateView.as_view(), name='card_product_create'),
    path('<str:category>/card_product/<slug:slug>/delete/', CardProductDeleteView.as_view(), name='card_product_delete'),
    path('<str:category>/card_product/<slug:slug>/update/', CardProductUpdateView.as_view(), name='card_product_update'),
    path('my_card_product/', MyCardProductView.as_view(), name='my_card_product'),
    path('<str:category>/card_product/<slug:slug>/', CardProductView.as_view(), name='card'),
]