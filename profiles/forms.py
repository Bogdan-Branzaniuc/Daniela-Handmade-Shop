from django import forms
from .models import UserProfile
from products.widgets import CustomClearableFileInput

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', 'google_profile_image')

    profile_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'address1': 'Street Address 1',
            'address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'profile_image': 'Profile Image',
        }

        self.fields['phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
