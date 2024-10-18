# products/views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products/product_list.html', {'products': products})

def segment_products(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000)
    min_size = request.GET.get('min_size', 0)
    max_size = request.GET.get('max_size', 100)

    products = Product.objects.filter(
        price__gte=min_price,
        price__lte=max_price,
        size__gte=min_size,
        size__lte=max_size
    )
    return render(request, 'products/segment.html', {'products': products})
