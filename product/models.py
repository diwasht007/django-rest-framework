from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class Store(models.Model):
    store_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.store_name

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255,blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/products', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products",null=True)

    def __str__(self):
        return self.product_name
    
class Review(models.Model):
    rating = models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments = models.CharField(max_length=200,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="Reviews",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " Rating of " +self.product.product_name + ":- " + str(self.rating)
    


    
    
