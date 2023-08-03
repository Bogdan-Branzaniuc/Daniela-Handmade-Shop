from .models import Product, Category, AvailableSizes, AvailableColors
from .widgets import CustomClearableFileInput
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    product_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AvailableSizesForm(forms.ModelForm):
    class Meta:
        model = AvailableSizes
        fields = ('size', 'expressed_in')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'size': 'add Size',
            'expressed_in': 'Category Size'
        }


class AvailableColorsForm(forms.Form):
    hexcolor = forms.CharField(max_length=7, empty_value='#FFF')