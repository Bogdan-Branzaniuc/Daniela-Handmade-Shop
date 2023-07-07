from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import get_object_or_404
import cloudinary.uploader
import cloudinary


def profile(request):
    '''
    A view to return the profile page profile.html
    '''
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        data = request.FILES
        image = data.get('profile_image')
        user_profile.profile_image = image
        user_profile.save()
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profiles/profile.html', context)
