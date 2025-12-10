from django.urls import path
from . import views

urlpatterns = [
    path('ejemplo', views.example_view),
]
