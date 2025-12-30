from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderProductSerializer, OrderSerializer
from .models import Order, OrderProduct
from .forms import OrderProductForm

# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user, 
            )
        
        form.instance.order = order
        form.save()
        return super().form_valid(form)

class OrderAPI(APIView):
    serializer_class = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data )
    
class OrderProductAPI(APIView):
    serializer_class = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        order = OrderProduct.objects.all()
        serializer = OrderProductSerializer(order, many=True)
        return Response(serializer.data )