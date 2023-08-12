from django_unicorn.components import UnicornView
from products.models import AvailableSize
from django.contrib import messages


class SizeBySizecategoryChoiceFieldView(UnicornView):

    available_sizes = None
    standard_sizes = []
    infant_sizes = []
    shoe_sizes = []
    product = None

    selected_size_category = None
    selected_standard_sizes = []
    selected_infant_sizes = []
    selected_shoe_sizes = []
    final_sizes = []

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.selected_size_category = 'universal'
        self.final_sizes = ['U']
        self.standard_sizes = []
        self.infant_sizes = []
        self.shoe_sizes = []

    def mount(self):
        """
        1- mounts the existing product if editing one, and sets the sellectors to properly render the component template
        2- creates lists of possible future selections based on the AvailableSizes model's field SIZE_CHOICES
        """
        if self.product:
            product_sizes = [size.size for size in self.product.sizes.all()]
            for choice_tuple in AvailableSize.SIZE_CHOICES:
                if product_sizes[0] == choice_tuple[0]:
                    self.selected_size_category = choice_tuple[1].split('_')[1]
            if self.selected_size_category == 'standard':
                self.selected_standard_sizes = product_sizes
            elif self.selected_size_category == 'infant':
                self.selected_infant_sizes = product_sizes
            elif self.selected_size_category == 'shoe':
                self.selected_shoe_sizes = product_sizes

            self.final_sizes = product_sizes

        for size_tuple in AvailableSize.SIZE_CHOICES:
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
