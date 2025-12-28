from django.contrib import admin # <- viene por defecto
from .models import product

# Register your models here.
class ProductAdmin(admin.ModelAdmin): # Superclase para administrar modelos
    model: 'product' # Decorador
    list_display = ('name', 'price', 'available') # Campos a mostrar en la lista
    search_fields = ('name',)  # Campos para la búsqueda
    list_filter = ('available',)  # Filtros laterales

# Registro del modelo con la configuración personalizada
admin.site.register(product, ProductAdmin)



