from django.shortcuts import render

from .models import Product
# Create your views here.

def homeView(request):
    prods = Product.objects.all() # SELECT * FROM mainapp_product;
    context = {
        'products' : prods

    }
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context


