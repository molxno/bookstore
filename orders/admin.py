from django.contrib import admin

from orders.models import Order, OrderBook


# Register your models here.
class OrderProductInLine(admin.TabularInline):
    model = OrderBook
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInLine]


admin.site.register(Order, OrderAdmin)
