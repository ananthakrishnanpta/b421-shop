from django.shortcuts import render, redirect
from .models import CartItem
from mainapp.models import Product

# Create your views here.

# 1. C
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)

    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    
    cart_item.save()

    return redirect('view_cart')

# 2. R 

def viewCart(request):
    # select * from cartitem where id = request.user.id;
    items = CartItem.objects.filter(user = request.user)
    total_price = sum([item.sub_total() for item in items])
    context = {
        'cart_items' : items,
        'total_price' : total_price
    }
    template = 'view_cart.html'

    return render(request, template, context)


# U

def addQuantity(request, cart_item_id):

    pass 

def remQuantity(request, cart_item_id):
    pass



# D

def remFromCart(request, cart_item_id):
    
    this_item = CartItem.objects.get(id = cart_item_id)
    this_item.delete() # delete from cartitem where id = cart_item_id

    return redirect('view_cart')

