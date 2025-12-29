from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import product
from .forms import ProductForm


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = product
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductFormView(FormView):
    template_name = "products/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListAPI(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        products = product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)