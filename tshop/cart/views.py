from django.shortcuts import render, redirect
from .models import CartItem
from mainapp.models import Product

# implementing AJAX to update cart item quantity without refresh
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
# Create your views here.

# 1. C

@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)

    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    
    cart_item.save()

    return redirect('view_cart')

# 2. R 
@login_required
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
@login_required
def addQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    overall_total = sum(item.sub_total() for item in CartItem.objects.filter(user=request.user))
    return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.sub_total(), 'overall_total': overall_total})

@login_required
def remQuantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        overall_total = sum(item.sub_total() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': cart_item.quantity, 'total_price': cart_item.sub_total(), 'overall_total': overall_total})
    else:
        cart_item.delete()
        overall_total = sum(item.sub_total() for item in CartItem.objects.filter(user=request.user))
        return JsonResponse({'quantity': 0, 'total_price': 0, 'overall_total': overall_total})

# D
@login_required
def remFromCart(request, cart_item_id):
    
    this_item = CartItem.objects.get(id = cart_item_id)
    this_item.delete() # delete from cartitem where id = cart_item_id

    return redirect('view_cart')

