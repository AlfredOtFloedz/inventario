from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Producto

@receiver(pre_save, sender=Producto)

def update_updated_at(sender, instance, **kwargs):
    print("señal activada")
    if instance.pk is not None:
        old_producto = Producto.objects.get(pk=instance.pk)
        if old_producto.precio != instance.precio:
            
            print("El precio ha cambiado, actualizando updated_at")
            instance.price_update = timezone.now()
            print(instance.price_update)
