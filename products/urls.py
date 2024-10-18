# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Default path for products
    path('segment/', views.segment_products, name='segment_products'),
]
