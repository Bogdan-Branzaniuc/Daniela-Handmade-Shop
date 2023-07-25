from django_unicorn.components import UnicornView
import time

class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """
    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def update(self):
        time.sleep(0.2)
        self.bag = self.request.session.get('bag', {})
        print(self.bag)