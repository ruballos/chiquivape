from django.contrib import admin

from .models import DetalleVenta, Venta, Tienda, Caracteristica, Categoria, Marca, Producto, Pedido_Ingreso, DetallePedido, Caracteristica_Articulo
# Register your models here.
admin.site.register(Tienda)
admin.site.register(Caracteristica)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Pedido_Ingreso)
admin.site.register(DetallePedido)
admin.site.register(Caracteristica_Articulo)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
