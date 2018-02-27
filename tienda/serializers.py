from rest_framework import serializers

from .models import DetalleVenta, Venta, Producto, Tienda, Categoria, Caracteristica, Marca, Pedido_Ingreso, DetallePedido, Caracteristica_Articulo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_staff')

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ("__all__")

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = ("__all__")

class CategoriaSerializer(serializers.ModelSerializer):
    caracteristica = CaracteristicaSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ("__all__")

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ("__all__")

class ProductoSerializer(serializers.ModelSerializer):
    tienda = TiendaSerializer()
    categoria = CategoriaSerializer()
    marca = MarcaSerializer()
    class Meta:
        model = Producto
        fields = ("__all__")

#Pedido:
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Ingreso
        fields = ("__all__")

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ("__all__")

class CaractArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica_Articulo
        fields = ("__all__")

#Detalle de pedido sólo lectura

class CategoriaSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("__all__")

class ProductoSerializerRead(serializers.ModelSerializer):
    tienda = TiendaSerializer()
    categoria = CategoriaSerializerRead()
    marca = MarcaSerializer()
    class Meta:
        model = Producto
        fields = ("__all__")

class DetallePedidoSerializerRead(serializers.ModelSerializer):
    producto=ProductoSerializerRead()
    caracteristica_articulo=CaractArticuloSerializer(many=True)
    class Meta:
        model = DetallePedido
        fields = ("__all__")

class PedidoDetalleSerializer(serializers.ModelSerializer):
    detalle_pedido=DetallePedidoSerializerRead(many=True)
    class Meta:
        model = Pedido_Ingreso
        fields = ("__all__")

#foto
class ProductoSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("__all__")

#producto save
class ProductoSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("__all__")

#detalle ingreso
class DetallePedidoSerializerList(serializers.ModelSerializer):
    caracteristica_articulo=CaractArticuloSerializer(many=True)
    class Meta:
        model = DetallePedido
        fields = ("__all__")

class ProductoSerializerExistencia(serializers.ModelSerializer):
    detalle_producto=DetallePedidoSerializerList(many=True)
    class Meta:
        model = Producto
        fields = ("__all__")

#aperturar venta y detalle_venta
class VentaApertura(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ("__all__")

class DetalleVentaSave(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ("__all__")


#producto select Venta
class InventarioExistencia(serializers.ModelSerializer):
    producto=ProductoSerializer()
    caracteristica_articulo=CaractArticuloSerializer(many=True)
    class Meta:
        model = DetallePedido
        fields = ("__all__")

#venta detallado
class DetallePedidoSerializer2(serializers.ModelSerializer):
    producto=ProductoSerializer()
    caracteristica_articulo=CaractArticuloSerializer(many=True)
    class Meta:
        model = DetallePedido
        fields = ("__all__")

class DetalleVentaSerializer(serializers.ModelSerializer):
    detalle_pedido=DetallePedidoSerializer2()
    class Meta:
        model = DetalleVenta
        fields = ("__all__")

class VentaSerializer(serializers.ModelSerializer):
    venta_detalle=DetalleVentaSerializer(many=True)
    class Meta:
        model = Venta
        fields = ("__all__")
