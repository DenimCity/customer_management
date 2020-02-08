from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders, 'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        "delivered": delivered,
        "pending": pending
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


def customers(request):
    return render(request, 'accounts/customer.html')

# This is and example of a backend api call

# def customer(request):
#     print(request)
#     return HttpResponse('customer')
