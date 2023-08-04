from django_unicorn.components import UnicornView
from products.models import AvailableSizes
from django.contrib import messages

class SizeBySizecategoryChoiceFieldView(UnicornView):

    selected_size_category = None
    available_sizes = None
    universal_sizes = None
    standard_sizes = []
    infant_sizes = []
    shoe_sizes = []

    selected_standard_sizes = []
    selected_infant_sizes = []
    selected_shoe_sizes = []
    final_sizes = []
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.selected_size_category = 'universal'
        self.final_sizes = ['U']
        self.standard_sizes = []
        self.infant_sizes = []
        self.shoe_sizes = []


    def mount(self):
        for size_tuple in AvailableSizes.SIZE_CHOICES:
            if size_tuple[1].split('_')[1] == 'standard':
                self.standard_sizes.append(size_tuple[0])
            elif size_tuple[1].split('_')[1] == 'infant':
                self.infant_sizes.append(size_tuple[0])
            elif size_tuple[1].split('_')[1] == 'shoe':
                self.shoe_sizes.append(size_tuple[0])

    def select_category_size(self, size_category):
        """
            if the user presses twice on the size_category button, his selections will not be affected
        """
        self.selected_size_category = size_category
        if size_category == 'universal':
            self.selected_infant_sizes = self.selected_shoe_sizes = self.selected_standard_sizes = []
            self.final_sizes = ['U']
        elif size_category == 'standard':
            self.selected_infant_sizes = self.selected_shoe_sizes = []
        elif size_category == 'infant':
            self.selected_standard_sizes = self.selected_shoe_sizes = []
        elif size_category == 'shoe':
            self.selected_standard_sizes = self.selected_infant_sizes = []

    def toggle_selected_standard_size(self, size):
        if size not in self.selected_standard_sizes:
            self.selected_standard_sizes.append(size)
        else:
            self.selected_standard_sizes.remove(size)
        self.final_sizes = self.selected_standard_sizes

    def toggle_selected_infant_size(self, size):
        if size not in self.selected_infant_sizes:
            self.selected_infant_sizes.append(size)
        else:
            self.selected_infant_sizes.remove(size)

        self.final_sizes = self.selected_infant_sizes

    def toggle_selected_shoe_size(self, size):
        if size not in self.selected_shoe_sizes:
            self.selected_shoe_sizes.append(size)
        else:
            self.selected_shoe_sizes.remove(size)

        self.final_sizes = self.selected_shoe_sizes


