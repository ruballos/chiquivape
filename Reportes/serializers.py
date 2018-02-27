from rest_framework import serializers

from tienda.models import DetalleVenta, Venta, Producto, Tienda, Categoria, Caracteristica, Marca, Pedido_Ingreso, DetallePedido, Caracteristica_Articulo


#venta
class R_Categoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("__all__")

class R_Marca(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ("__all__")

class R_Producto(serializers.ModelSerializer):
    categoria = R_Categoria()
    marca = R_Marca()
    class Meta:
        model = Producto
        fields = ("__all__")


class R_DetallePedido(serializers.ModelSerializer):
    producto=R_Producto()
    class Meta:
        model = DetallePedido
        fields = ("__all__")

class R_Venta(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ("__all__")

class R_DetalleVenta(serializers.ModelSerializer):
    venta=R_Venta()
    detalle_pedido=R_DetallePedido()
    class Meta:
        model = DetalleVenta
        fields = ("__all__")
