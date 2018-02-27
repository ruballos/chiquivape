"""vape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from tienda.views import InventarioAgotarView, UserView, VentaDetallada, DetalleVentaSave, InventarioExistenciaView, VentaView, ProductoExistencia, ProductoSave, CategoriaView, MarcaView, ProductosView,ProductosPutView, PedidosView, DetallePedidoView, CaracteristicaArticuloView, PedidoDetalleView
from Reportes.views import ReporteInventarioPDF, ReporteVentasPDF
from Reportes.views import R_Ventas
rutasTienda = DefaultRouter()
rutasTienda.register(r'productos', ProductosView)
rutasTienda.register(r'productosput', ProductosPutView)
rutasTienda.register(r'pedidos', PedidosView)
rutasTienda.register(r'detalle_pedido', DetallePedidoView)
rutasTienda.register(r'caracteristica_articulo', CaracteristicaArticuloView)
rutasTienda.register(r'pedido_detallado', PedidoDetalleView)
rutasTienda.register(r'marcas', MarcaView)
rutasTienda.register(r'categorias', CategoriaView)
rutasTienda.register(r'productosave', ProductoSave)
rutasTienda.register(r'productoexistencia', ProductoExistencia)
rutasTienda.register(r'venta', VentaView)
rutasTienda.register(r'existencias', InventarioExistenciaView)
rutasTienda.register(r'agotar', InventarioAgotarView)
rutasTienda.register(r'detalleventasave', DetalleVentaSave)
rutasTienda.register(r'ventadetalle', VentaDetallada)
rutasTienda.register(r'user', UserView, 'user')

rutasReportes = DefaultRouter()
rutasReportes.register(r'ventas', R_Ventas, 'ventas')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    url(r'^tienda/', include(rutasTienda.urls)),

    url(r'^reportes/', include(rutasReportes.urls)),

    url(r'^inventario/$',ReporteInventarioPDF.as_view(), name="inventario"),
    url(r'^ventas/$',ReporteVentasPDF.as_view(), name="ventas"),
]

"""para las imagenes"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
