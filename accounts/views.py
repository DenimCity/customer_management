from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print("Hi Its me OHHHHHHHH SNAP I HAVE A LOG")
    return render(request, 'accounts/dashboard.html')


def products(request):
    print(request)
    return HttpResponse('products')

# This is and example of a backend api call


def customer(request):
    print(request)
    return HttpResponse('customer')
