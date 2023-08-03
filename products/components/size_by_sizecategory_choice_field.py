from django_unicorn.components import UnicornView
from products.models import AvailableSizes
from django.contrib import messages

class SizeBySizecategoryChoiceFieldView(UnicornView):

    selected_size_category = None
    available_sizes = None
    def mount(self):
        self.selected_size_category = 'universal'