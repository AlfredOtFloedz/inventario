from django import forms
from . models import Producto, Order

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['code', 'name', 'category', 'quantity', 'precio']
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity', 'customer']
   