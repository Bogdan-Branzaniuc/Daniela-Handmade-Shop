from django_unicorn.components import UnicornView


class BagstatusView(UnicornView):
    def mount(self, *args, **kwargs):
        return super().mount()

    def add_to_bag(self, product_id):
        bag = self.request.session.get('bag', {})
        bag[product_id] = 1
        print(bag)
