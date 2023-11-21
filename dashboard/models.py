from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY = (
    ('Minisplit', 'Minisplit'),
    ('Boiler', 'Boiler'),
    ('Ferreteria', 'Ferreteria'),
)

class Producto(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=1000.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    price_update = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE)
    order_quantity = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100, default=None)
    
    #Cambiar etiqueta en la barra de lateral Pedido ---> Ventas
    class Meta:
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f'{self.product} pedido realizado por {self.staff.username}'