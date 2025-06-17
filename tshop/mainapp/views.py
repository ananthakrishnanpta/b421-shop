from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

# Importing generic Class Based Views (CBV)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Product
# Create your views here.

# To check for authentication
from django.contrib.auth.mixins import LoginRequiredMixin

# CRUD operations of Product model

# 1. Create (Insert statements)

class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'add_product.html'
    success_url = '/'

# 2 Read (Select statements)
    # List view
def homeView(request):
    prods = Product.objects.all() # SELECT * FROM mainapp_product;
    context = {
        'products' : prods,
        'search_bar' : True

    }
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context

    # Detail view 
class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'

# 3. Update view (Update statement)
class EditProduct(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'edit_product.html'
    success_url = '/'

# 4. Delete view (Delete statement)
class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'




def searchView(request):
    query = request.GET.get('search_text')

    result_products = Product.objects.filter(name__icontains = query)
    context =  {
        'products' : result_products,
        'query' : query,
        'search_bar' : True
    }

    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))
