from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print(request)
    return HttpResponse('home')


def products(request):
    print(request)
    return HttpResponse('products')


def customer(request):
    print(request)
    return HttpResponse('customer')
