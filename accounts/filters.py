import django_filters
from order.models import Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'created_at']
