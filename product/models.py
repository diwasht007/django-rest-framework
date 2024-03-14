from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255,blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/products', blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
