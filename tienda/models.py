from django.db import models

# Create your models here.
class Tienda(models.Model):
    ciudad = models.CharField(max_length=100, default='', blank=True)
    estado = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return '%s' % (self.ciudad)


#Producto:
class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return '%s' % (self.caracteristica)

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, default='', blank=True)
    caracteristica = models.ManyToManyField(Caracteristica)
    estado = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return '%s' % (self.categoria)

class Marca(models.Model):
    nombre = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return '%s' % (self.nombre)

class Producto(models.Model):
    def upload_path_handler(instance, filename):
        ext = filename.split('.')[-1]
        return "admon/imagenes/productos/{id}.{ext}".format(id=instance.pk, ext=ext)

    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, default='1',)
    nombre = models.CharField(max_length=200, default='', blank=True)
    descripcion = models.CharField(max_length=250, default='', blank=True)
    precio_costo = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
    stock = models.IntegerField(default=0, blank=False, null=True)
    estado = models.BooleanField(default=True, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(
    blank=True,
    upload_to=upload_path_handler,
    )

    def __str__(self):
        return '%s - %s' % (self.nombre, self.marca)


#Pedido:

class Pedido_Ingreso(models.Model):
    fecha_ingreso = models.DateField(auto_now=True, blank=False)
    descripcion = models.CharField(max_length=250, default='', blank=True)

    def __str__(self):
        return '%s' % (self.fecha_ingreso)

class DetallePedido(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, related_name='detalle_producto')
    pedido_ingreso = models.ForeignKey(Pedido_Ingreso, on_delete=models.CASCADE, null=True, related_name='detalle_pedido')
    cantidad = models.IntegerField(default=1, blank=False, null=True)
    anotaciones = models.CharField(max_length=300, default='', blank=True)

    def __str__(self):
        return '%s' % (self.producto)

class Caracteristica_Articulo(models.Model):
    nombre = models.CharField(max_length=50, default='', blank=True)
    valor = models.CharField(max_length=50, default='', blank=True)
    articulo = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='caracteristica_articulo')

    def __str__(self):
        return '%s' % (self.nombre)


#Venta:

class Venta(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, default='1', null=True, blank=True)
    fecha_venta = models.DateField(auto_now=True, blank=False)
    descripcion = models.CharField(max_length=250, default='', blank=True)
    detalle_venta = models.ManyToManyField(DetallePedido, through='DetalleVenta', related_name='detalleventa')
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
    estado = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return '%s' % (self.fecha_venta)

class DetalleVenta(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='detallepedido')
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='venta_detalle')
    cantidad = models.IntegerField(default=1, blank=False, null=True)
    precio_costo = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
    precio_venta = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=00.00)
