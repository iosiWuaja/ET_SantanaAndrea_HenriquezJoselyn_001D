from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nombre_prod = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    precio = models.CharField(max_length=10)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos_fotos/', blank=True, null=True)

    def __str__(self):
        return str(self.nombre_prod)+" "+str(self.descripcion)  

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'