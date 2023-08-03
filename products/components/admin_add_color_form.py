from django_unicorn.components import UnicornView
from products.forms import AvailableColorsForm

class AdminAddColorFormView(UnicornView):

    form_class = AvailableColorsForm

    value = None
    def mount(self):
        self.value = 1


