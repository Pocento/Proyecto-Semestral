from django.db import models
# Create your models here.
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=60)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(null=True, blank=True)
   
    def __str__(self):
        return self.nombre
