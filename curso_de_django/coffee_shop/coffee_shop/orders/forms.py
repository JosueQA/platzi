from .models import OrderProduct
from django.forms import ModelForm

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']