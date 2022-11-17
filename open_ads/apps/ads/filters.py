import django_filters
from mptt.forms import TreeNodeChoiceField
from apps.ads.models import Card
from apps.categories.models import Category


class CardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    id_user__city = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Card
        fields = {'id_category', 'title', 'id_user__city'}