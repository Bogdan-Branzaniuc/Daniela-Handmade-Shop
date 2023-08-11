from .models import Product, Category, AvailableColors
from .widgets import CustomClearableFileInput, CustomCheckboxSelectMultiple
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['sizes']

    colors = forms.ModelMultipleChoiceField(
        label='Colors',
        queryset=AvailableColors.objects.all(),
        widget=CustomCheckboxSelectMultiple
    )
    product_image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)
    # available_colors = forms.MultipleChoiceField(label='colors', required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



