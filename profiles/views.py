from django.shortcuts import render


def profile(request):
    '''
    A view to return the home page index.html
    '''
    return render(request, 'profiles/profile.html')
