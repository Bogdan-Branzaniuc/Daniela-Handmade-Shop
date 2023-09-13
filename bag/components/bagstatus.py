from django_unicorn.components import UnicornView
import time

class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the 
    bag session
    """
    name = 'bagstatus'
    bag = dict

    def mount(self, *args, **kwargs):
        self.update()
        return super().mount()

    def update(self):
        self.bag = self.request.session.get('bag', {})