from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path(' ', HttpResponse("Hello, this is the car list page.")),
]
