from django_filters import rest_framework as filters
from cards.models import Card


class CardFilter(filters.FilterSet):
    min_credit = filters.NumberFilter(field_name='credit', lookup_expr='gte')
    max_credit = filters.NumberFilter(field_name='credit', lookup_expr='lte')
    series = filters.CharFilter(field_name='series', lookup_expr='icontains')
    number = filters.CharFilter(field_name='number', lookup_expr='icontains')

    class Meta:
        model = Card
        fields = {
            'status': ['in', 'exact']
        }
