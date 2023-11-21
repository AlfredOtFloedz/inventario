from django.contrib import admin
from . models import Producto, Order
from django.contrib.auth.models import Group

admin.site.site_header = "Pro Aires"

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'quantity','category')
    list_filter = ('category',) #['category'] 

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Order)
#admin.site.unregister(Group) 