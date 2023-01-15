from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venta')
    cliente = models.CharField(max_length=50)
    dnicliente = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    total = models.IntegerField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Venta n°: {self.idventa}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Pertenece a: {self.venta}'

class Deposito(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendedor', blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidadp = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.timestamp}'