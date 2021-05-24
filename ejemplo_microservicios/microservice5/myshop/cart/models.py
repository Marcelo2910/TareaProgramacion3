
from django.db import models
from django.urls import reverse

class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock = models.PositiveIntegerField(null=True)
    available = models.BooleanField(default=True)

    # Clase Meta en donde se indican campos para ordenamiento y el index entre el id y el slug.
    class Meta:
        index_together = (('id'),)

    # Método to String de la clase, la cual es representada por el campo 'name'.
    def __str__(self):
        return self.name

    # Método que regresa la url absoluta del modelo, la cual contiene los campos 'id' y 'slug'.
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

class Cart (models.Model):
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return "Carrito de: "+self.usuario
    
class ProductoCarrito( models.Model):
    carrito_id = models.ForeignKey(Cart, related_name='carrito', on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Product, related_name='producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()