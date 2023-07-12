from django_unicorn.components import UnicornView


class ProductView(UnicornView):

    def mount(self, *args, **kwargs):
        return super().mount()

    def product_test(self, product_id):
        bag = self.request.session.get('bag', {})
        bag[product_id] = 1
        print(bag)
