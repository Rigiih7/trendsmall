from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Products, Laptops

# Create your views here.
def index(request):

    products = Products.objects.all()

    laptops = Laptops.objects.all()
    
    return render(request, "index.html", {'products' : products, 'laptops' : laptops})

def singleproduct(request, id):

    product = Products.objects.filter(id = id).first()
    laptop = Laptops.objects.filter(id = id).first()

    if product:
        data_source = 'product'
    elif laptop:
        data_source = 'laptop'
    else:
        data_source = None

    context = {
        'product': product,
        'laptop' : laptop,
    }


    return render(request, "singleproduct.html", context)

def shoppingcart(request):
    
    return render(request, 'shopping-cart.html')

   