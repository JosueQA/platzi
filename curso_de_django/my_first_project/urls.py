from django.contrib import admin
from django.urls import path
from my_first_app.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carlist/', my_view, name='carlist'),
]
