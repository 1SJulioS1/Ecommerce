import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    min_quantity = django_filters.NumberFilter(
        field_name='quantity', lookup_expr='gte')
    max_quantity = django_filters.NumberFilter(
        field_name='quantity', lookup_expr='lte')
    start_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte')
    start_updated = django_filters.DateFilter(
        field_name='updated_at', lookup_expr='gte')
    end_updated = django_filters.DateFilter(
        field_name='updated_at', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []


class OrderFilter(django_filters.FilterSet):
    start_created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte')
    end_created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte')
    start_updated_at = django_filters.DateFilter(
        field_name='updated_at', lookup_expr='gte')
    end_updated_at = django_filters.DateFilter(
        field_name='updated_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = []
