from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



from product.models import Product

User = get_user_model()

# Create your models here.


class Carts(models.Model):
    user = models.OneToOneField(User, related_name='cart' , on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    update_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Carts.objects.create(user=instance)







    