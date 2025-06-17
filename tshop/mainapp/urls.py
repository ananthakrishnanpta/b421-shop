from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name = 'homepage'),
    path('product/<int:pk>', views.ProductDetails.as_view(), name = 'prod_detail'),
    path('product/add', views.AddProduct.as_view(), name = 'add_prod'),
    path('product/edit/<int:pk>', views.EditProduct.as_view(), name = 'edit_prod'),
    path('product/del/<int:pk>', views.DeleteProduct.as_view(), name = 'del_prod'),
    path('products/search', views.searchView, name = 'search')
]