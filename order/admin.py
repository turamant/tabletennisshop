from django.contrib import admin

# Register your models here.
from order.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name', 'email','address', 'zipcode', 'place',
                    'phone', 'created_at', 'paid','paid_amount', 'status')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
