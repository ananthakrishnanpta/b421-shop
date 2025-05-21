from django.shortcuts import render

# Create your views here.

def homeView(request):
    context = {}
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context


