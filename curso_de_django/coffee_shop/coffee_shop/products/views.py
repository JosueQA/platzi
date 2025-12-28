from django.urls import reverse_lazy
from .models import product
from django.views.generic import TemplateView, FormView, ListView
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
