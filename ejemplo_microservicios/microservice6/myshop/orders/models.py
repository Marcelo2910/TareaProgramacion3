from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    # Clase Meta en donde se indican campos para ordenamiento y el verbose name.
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # Método to String de la clase, la cual es representada por el campo 'name'.
    def __str__(self):
        return self.name

    # Método que regresa la url absoluta del modelo, la cual contiene el campo 'slug'.
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Clase Meta en donde se indican campos para ordenamiento y el index entre el id y el slug.
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    # Método to String de la clase, la cual es representada por el campo 'name'.
    def __str__(self):
        return self.name

    # Método que regresa la url absoluta del modelo, la cual contiene los campos 'id' y 'slug'.
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    # Clase Meta en donde se indican campos para ordenamiento.
    class Meta:
        ordering = ('-created',)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return 'Order {}'.format(self.id)

    # Método que obtiene el costo total de la orden.
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return '{}'.format(self.id)

    # Método que obtiene el costo total del item de la orden.
    def get_cost(self):
        return self.price * self.quantity