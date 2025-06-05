from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:product_id>', views.addToCart, name = 'add_to_cart'),
    path('', views.viewCart, name = 'view_cart'),
    path('rem/<int:cart_item_id>', views.remFromCart, name = 'rem_from_cart')
]