from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import get_object_or_404


@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profiles'))
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user_profile': user_profile
    }
    return render(request, template, context)

