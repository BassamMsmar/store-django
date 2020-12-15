from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):

    title = models.CharField( max_length=100)
    brand = models.CharField( max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField( max_length=200)
    image = models.ImageField(upload_to='product' , null = True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse("product_details", kwargs={"pk": self.pk})


