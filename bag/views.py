from django.shortcuts import render, get_object_or_404
from products.models import Product


def bag(request):
    '''
    A view to return the home page index.html
    '''
    product = get_object_or_404(Product, id=1)

    context = {
        'product': product,
    }

    return render(request, 'products/products.html', context)
