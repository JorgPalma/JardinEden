from django.contrib import admin
from .models import Perfil, Producto, Venta, Deposito, Categoria, DetalleVenta

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Deposito)