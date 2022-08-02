from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Product


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})
