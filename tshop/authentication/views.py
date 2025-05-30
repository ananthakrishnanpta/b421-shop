from django.shortcuts import render

# importing the inbuilt User model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy # finds the url path associated with a url name

from django.views.generic import CreateView

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'signin.html'
    success_url = '/'

class UserRegisterView(CreateView):
    model = User 
    template_name = 'signup.html'
    fields = '__all__'
    success_url = reverse_lazy('signin') # redirects user to login page after registeration
