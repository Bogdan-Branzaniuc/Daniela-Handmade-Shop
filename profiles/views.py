from django.shortcuts import render
from .models import UserProfile
from .forms import UserProfileForm
from django.shortcuts import get_object_or_404


def profile(request):
    '''
    A view to return the profile page profile.html
    '''
    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
    else:
        user_profile = 'none'
    user_profile_form = UserProfileForm()
    if request.method == "POST":
        data = request.FILES
        image = data.get('profile_image')

        user_profile.profile_image = image
        user_profile.save()
    else:
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile_form = UserProfileForm(initial={
                    'phone_number': user_profile.phone_number,
                    'postcode': user_profile.postcode,
                    'town_or_city': user_profile.town_or_city,
                    'address1': user_profile.address1,
                    'address2': user_profile.address2,
                    'county': user_profile.county,
                })
            except UserProfile.DoesNotExist:
                user_profile_form = UserProfileForm()
        else:
            user_profile_form = UserProfileForm()
    context = {
        'user_profile': user_profile,
        'user_profile_form': user_profile_form,
    }
    return render(request, 'profiles/profile.html', context)
