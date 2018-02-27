from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Venta, DetalleVenta, Categoria, Producto, Pedido_Ingreso, DetallePedido, Caracteristica_Articulo, Marca
from .serializers import UserSerializer, VentaSerializer, DetalleVentaSave, InventarioExistencia, VentaApertura, ProductoSerializerExistencia, ProductoSerializerSave, CategoriaSerializer, ProductoSerializer, PedidoSerializer, DetallePedidoSerializer, CaractArticuloSerializer, PedidoDetalleSerializer, ProductoSerializerPut, MarcaSerializer

from rest_framework import status
from rest_framework.response import Response
from django.db.models import F
# Create your views here.

class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = User.objects.all().filter(username=self.request.user)
        return queryset


class ProductosView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()


class PedidosView(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pedido_Ingreso.objects.all().order_by('fecha_ingreso').reverse()


class DetallePedidoView(viewsets.ModelViewSet):
    serializer_class = DetallePedidoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = DetallePedido.objects.all()

class CaracteristicaArticuloView(viewsets.ModelViewSet):
    serializer_class = CaractArticuloSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Caracteristica_Articulo.objects.all()

#Detalle pedidos
class PedidoDetalleView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PedidoDetalleSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pedido_Ingreso.objects.all()

#foto
class ProductosPutView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializerPut
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()

#marcas
class MarcaView(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Marca.objects.all()

#categorias
class CategoriaView(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()

#producto save
class ProductoSave(viewsets.ModelViewSet):
    serializer_class = ProductoSerializerSave
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()

#producto detalle existencia
class ProductoExistencia(viewsets.ModelViewSet):
    serializer_class = ProductoSerializerExistencia
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()

#venta aperturar y detalle_venta
class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaApertura
    permission_classes = (IsAuthenticated,)
    queryset = Venta.objects.all()

class DetalleVentaSave(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSave
    permission_classes = (IsAuthenticated,)
    queryset = DetalleVenta.objects.all()

    def destroy(self, request, *args, **kwargs):
        detalleventa = DetalleVenta.objects.get(pk=self.kwargs['pk'])
        DetallePedido.objects.filter(pk=detalleventa.detalle_pedido.pk).update(cantidad = F('cantidad') + detalleventa.cantidad )

        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


    def create(self, request, *args, **kwargs):
        DetallePedido.objects.filter(pk=request.data['detalle_pedido']).update(cantidad = F('cantidad') - request.data['cantidad'] )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#select producto Venta
class InventarioExistenciaView(viewsets.ModelViewSet):
    serializer_class = InventarioExistencia
    permission_classes = (IsAuthenticated,)
    queryset = DetallePedido.objects.all().exclude(cantidad=0)

#venta detallada
class VentaDetallada(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Venta.objects.all()


#a agotar
from django.db.models import Q

class InventarioAgotarView(viewsets.ModelViewSet):
    serializer_class = InventarioExistencia
    permission_classes = (IsAuthenticated,)
    queryset = DetallePedido.objects.all().exclude(cantidad__gt=1).exclude(cantidad=0)
