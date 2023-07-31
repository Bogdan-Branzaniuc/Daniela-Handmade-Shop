from django_unicorn.components import UnicornView

class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """
    request = None
    name = 'bagstatus'
    bag = None

    def mount(self, *args, **kwargs):
        self.update()
        print(self.component_id)
        return super().mount()

    def update(self):
        self.bag = self.request.session.get('bag', {})

    