from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import settings
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )