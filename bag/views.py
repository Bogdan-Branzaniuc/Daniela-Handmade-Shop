from django.shortcuts import render

def bag(request):
    '''
    A view to return the bag page bag.html
    '''

    size_units = {
        '0-6': 'months',
        '6-12': 'months',
        '12-18': 'months',
        '18-24': 'months',
        '2-4': 'years',
        '24-30': 'EU',
        '30-35': 'EU',
        '35-38': 'EU',
        '38-43': 'EU',
    }
    context = {
        'size_units': size_units,
    }

    return render(request, 'bag/bag.html', context)
