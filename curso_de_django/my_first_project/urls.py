from django.contrib import admin
from django.urls import include, path
from my_first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('my_first_app.urls')),
    path('carros_con_clase/', views.CarListView.as_view()),
    path('lista/<int:id>', views.my_dinamic_view),
]
