from django.shortcuts import render

# importing the inbuilt User model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy # finds the url path associated with a url name

from django.views.generic import CreateView

from .forms import CustomLoginForm, CustomRegistrationForm
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class  = CustomLoginForm
    

class UserRegisterView(CreateView):
    model = User 
    form_class = CustomRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin') # redirects user to login page after registeration
