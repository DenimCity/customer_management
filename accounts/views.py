from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


def customers(request):
    return render(request, 'accounts/customer.html')

# This is and example of a backend api call

# def customer(request):
#     print(request)
#     return HttpResponse('customer')
