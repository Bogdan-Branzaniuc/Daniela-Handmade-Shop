from django_unicorn.components import UnicornView

class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """
    def mount(self, *args, **kwargs):
        self.update()
        return super().mount()

    def update(self):
        self.bag = self.request.session.get('bag', {})

        print('bagstatus', self.bag)
