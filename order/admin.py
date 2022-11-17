from django.contrib import admin

from .models import Order, OrderItem

class OrderItemTabuler(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'paid_amount',
                    'first_name', 'last_name', 'address', 'phone', 'created_at']
    list_filter = ['paid_amount', 'created_at']
    raw_id_fields = ['user']
    list_editable = ['paid_amount']
    inlines = [OrderItemTabuler]
    list_per_page = 24