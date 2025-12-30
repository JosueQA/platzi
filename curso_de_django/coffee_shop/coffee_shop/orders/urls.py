from django.urls import path
from .views import CreateOrderProductView, MyOrderView, OrderAPI, OrderProductAPI

urlpatterns = [
    path("my_order/", MyOrderView.as_view(), name="my_order"),
    path(
        "create_order_product/",
        CreateOrderProductView.as_view(),
        name="my_order_product",
    ),
    path("api/order", OrderAPI.as_view(), name="order_api"),
    path("api/order_products/", OrderProductAPI.as_view(), name="order_product_api"),
]
