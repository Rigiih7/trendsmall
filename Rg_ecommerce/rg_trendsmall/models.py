from django.db import models

# Create your models here.
class Products(models.model):
    image = models.ImageField(upload_to='images/products/large-size')
    name = models.CharField(max_length=100)
    price = models.IntegerField()