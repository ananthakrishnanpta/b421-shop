from django.shortcuts import render

# Importing generic Class Based Views (CBV)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Product
# Create your views here.

# CRUD operations of Product model

# 1. Create (Insert statements)
class AddProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'add_product.html'
    success_url = '/'

# 2 Read (Select statements)
    # List view
def homeView(request):
    prods = Product.objects.all() # SELECT * FROM mainapp_product;
    context = {
        'products' : prods

    }
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context

    # Detail view 
class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'

# 3. Update view (Update statement)
class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'edit_product.html'
    success_url = '/'

# 4. Delete view (Delete statement)
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'