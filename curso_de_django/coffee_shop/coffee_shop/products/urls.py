from django.urls import path
from . import views

urlpatterns = [
    # Listado de productos
    path(
        "",
        views.ProductListView.as_view(),
        {"title": "Listado de productos"},
        name="product_list",
    ),
    # Formulario para agregar productos
    path(
        "agregar/",
        views.ProductFormView.as_view(),
        name="product_form",
    ),
    path("api/", views.ProductListAPI.as_view(), name="product_list_api"),
]
