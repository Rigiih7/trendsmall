from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):

    products = Products.objects.all()
    
    return render(request, "index.html", {'products' : products})

    if not request.session.has_key("currency"):
        request.session["currency"] = settings.DEFAULT_CURRENCY

def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')    
    if request.method == 'post' :
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)




   