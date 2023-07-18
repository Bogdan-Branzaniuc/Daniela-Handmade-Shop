from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    '''
    A view to return the home page index.html
    '''
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
