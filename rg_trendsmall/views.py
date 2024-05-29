from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Laptops

# Create your views here.
def index(request):

    products = Products.objects.all()

    laptops = Laptops.objects.all()
    
    return render(request, "index.html", {'products' : products, 'laptops' : laptops})

def singleproduct(request, id):

    products = Products.objects.filter(id = id).first()

    context = {
        'products' : products,
    }

    laptops = Laptops.objects.filter(id = id).first()

    context = {
        'laptops' : laptops,
    }


    return render(request, "singleproduct.html", context)

def shoppingcart(request):
    
    return render(request, 'shopping-cart.html')

   