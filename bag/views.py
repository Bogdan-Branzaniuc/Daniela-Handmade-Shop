from django.shortcuts import render

def bag(request):
    '''
    A view to return the bag page bag.html
    '''

    context = {

    }

    return render(request, 'bag/bag.html', context)
