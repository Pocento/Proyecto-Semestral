from django.contrib import admin
from .models import TipoProducto, Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 3
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
