from django.contrib import admin
from orders.models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'user', 'is_active', 'order_date')
    list_filter = ('is_active', 'order_date')
    search_fields = ('user__username', 'id')
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)