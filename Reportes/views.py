from django.shortcuts import render

# Create your views here.
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View, ListView
from django.http import HttpResponse


from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table




from tienda.models import DetallePedido, DetalleVenta

class ReporteInventarioPDF(View):

    def get(self, request, *args, **kwargs):

        response = HttpResponse(content_type='application/pdf')
        pdf_name = "clientes.pdf"  # llamado clientes
        # la linea 26 es por si deseas descargar el pdf a tu computadora
        # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
        buff = BytesIO()
        doc = SimpleDocTemplate(buff,
                                pagesize=letter,
                                rightMargin=40,
                                leftMargin=40,
                                topMargin=60,
                                bottomMargin=18,
                                )


        clientes = []
        styles = getSampleStyleSheet()
        header = Paragraph("Inventario", styles['Heading2'])
        clientes.append(header)
        encabezados = ('Cant.', 'Producto', 'Marca')
        #Creamos una lista de tuplas que van a contener a las personas
        query =DetallePedido.objects.all().exclude(cantidad=0)
        existencias = [(detalle.cantidad, detalle.producto.nombre, detalle.producto.marca.nombre) for detalle in query]

        t = Table([encabezados] + existencias, colWidths=[60, 160, 160])
        t.setStyle(TableStyle(
            [
                ('GRID', (0, 0), (3, -1), 1, colors.black ),
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#7E7E7E') ),
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#CADF89') )
            ]
        ))
        clientes.append(t)
        doc.build(clientes)
        response.write(buff.getvalue())
        buff.close()
        return response


class ReporteVentasPDF(View):

    def get(self, request, *args, **kwargs):

        response = HttpResponse(content_type='application/pdf')
        pdf_name = "clientes.pdf"  # llamado clientes
        # la linea 26 es por si deseas descargar el pdf a tu computadora
        # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
        buff = BytesIO()
        doc = SimpleDocTemplate(buff,
                                pagesize=letter,
                                rightMargin=40,
                                leftMargin=40,
                                topMargin=60,
                                bottomMargin=18,
                                )

        clientes = []
        styles = getSampleStyleSheet()
        header = Paragraph("Ventas", styles['Heading2'])
        clientes.append(header)
        encabezados = ('Cant.', 'Producto', 'Marca', 'Precio Unitario', 'Total')
        #Creamos una lista de tuplas que van a contener a las personas
        query =DetalleVenta.objects.all()
        ventas = [(detalle.cantidad, detalle.detalle_pedido.producto.nombre, detalle.detalle_pedido.producto.marca.nombre, detalle.precio_venta, detalle.subtotal) for detalle in query]

        t = Table([encabezados] + ventas, colWidths=[50, 160, 100, 80, 60])
        t.setStyle(TableStyle(
            [
                ('GRID', (0, 0), (3, -1), 1, colors.black ),
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.HexColor('#7E7E7E') ),
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#CADF89') )
            ]
        ))
        clientes.append(t)
        doc.build(clientes)
        response.write(buff.getvalue())
        buff.close()
        return response



#ventas app reporte
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import R_DetalleVenta
from tienda.models import DetalleVenta

class R_Ventas(viewsets.ModelViewSet):
    serializer_class = R_DetalleVenta
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        fechade=self.request.META.get('HTTP_DE')
        fechaa=self.request.META.get('HTTP_A')
        queryset = DetalleVenta.objects.all().filter(venta__fecha_venta__range=(fechade, fechaa))
        return queryset
