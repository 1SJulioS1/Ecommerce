import django_filters
from django.contrib.auth import get_user_model

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


class CustomUserFilter(django_filters.FilterSet):
    last_login = django_filters.DateTimeFilter(field_name='last_login')
    username = django_filters.CharFilter(lookup_expr='icontains')
    active = django_filters.BooleanFilter(field_name='is_active')
    date_joined = django_filters.DateTimeFilter(field_name='date_joined')
    user_type = django_filters.ChoiceFilter(
        choices=get_user_model().USER_TYPE_CHOICES)

    class Meta:
        model = get_user_model()
        fields = []
