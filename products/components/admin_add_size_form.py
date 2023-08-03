from django_unicorn.components import UnicornView
from products.forms import AvailableSizesForm

class AdminAddSizeFormView(UnicornView):

    form_class = AvailableSizesForm

    value = None
    def mount(self):
        self.value = 1