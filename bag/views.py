from django.shortcuts import render, get_object_or_404
from products.models import Product


def bag(request):
    '''
    A view to return the bag page bag.html
    '''

    context = {}

    return render(request, 'bag/bag.html', context)
