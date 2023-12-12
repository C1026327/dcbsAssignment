from django.shortcuts import render
from .models import Module
# Create your views here.

def home(request):
    return render(request, 'itregistration/home.html', {'title':'Welcome'})


def about(request):
    return render(request, 'itregistration/about.html', {'title':'About Us'})

def contact(request):
    return render(request, 'itregistration/contact.html', {'title':'Contact Us'})

def modules(request):
    module = {'modules':Module.objects.all(), 'title': 'Modules'}
    return render(request, 'itregistration/modules.html', module)