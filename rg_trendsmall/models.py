from django.db import models
# Create your models here.
class Products(models.Model):
    image = models.ImageField(upload_to='images/products/large-size')
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    oldprice = models.IntegerField(null=True)
    discount_percentage = models.IntegerField(null=True)

class Laptops(models.Model):
    image = models.ImageField(upload_to='images/products/large-size')
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    oldprice = models.IntegerField(null=True)
    discount_percentage = models.IntegerField(null=True)

