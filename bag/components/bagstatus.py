from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404


class BagstatusView(UnicornView):

    bag = None
    grand_total = 0

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})

        return super().mount()

    def add_to_bag(self, product_id):
        product = get_object_or_404(Product, id=product_id)
        if product:
            self.grand_total += int(product.price)
        bag = self.request.session.get('bag', {})
        bag[product_id] = 1
        self.request.session['bag'] = bag
