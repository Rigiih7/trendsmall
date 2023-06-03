from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Laptops

# Create your views here.
def index(request):

    products = Products.objects.all()

    laptops = Laptops.objects.all()
    
    return render(request, "index.html", {'products' : products, 'laptops' : laptops})

def singleproduct(request):

    products = Products.objects.all()

    laptops = Laptops.objects.all()

    return render(request, "singleproduct.html", {'products' : products, 'laptops' : laptops})






   