from django.shortcuts import render


def checkout(request):
    """
    A view to return the bag page checkout.html
    """

    context = {

    }

    return render(request, 'checkout/checkout.html', context)
