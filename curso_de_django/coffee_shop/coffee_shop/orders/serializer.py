from rest_framework.serializers import ModelSerializer
from .models import Order, OrderProduct

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'is_active', 'order_date', 'total_cost', 'sub_total', 'IGV', 'orderproduct_set']

class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['order', 'product', 'quantity', 'total_price']