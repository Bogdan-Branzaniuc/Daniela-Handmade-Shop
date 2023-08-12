from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    A user profile model to collect and store all relevant user data from 
    all user authentication and input gates
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField(
        use_filename=True,
        unique_filename=False,
        folder='daniela_handmade/user_profile_images',
        null=True,
        blank=True,
    )
    google_profile_image = models.URLField(
        max_length=1000, null=True, blank=True,)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username
        
        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()
    # Existing users: just save the profile
    instance.userprofile.save()
