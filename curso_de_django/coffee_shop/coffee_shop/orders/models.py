from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from products.models import product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    @property
    def total_cost(self):
        return sum(item.total_price for item in self.orderproduct_set.all())
    
    @property
    def sub_total(self):
        return self.total_cost * Decimal(0.82)

    @property
    def IGV(self):
        return self.total_cost * Decimal(0.18)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.order} - {self.product}"
