from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product


class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    product = None
    bag = None

    def mount(self, *args, **kwargs):
        self.product = get_object_or_404(Product, id=1)
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def product_in_bag(self, product_id):

        if str(product_id) in self.bag.keys():
            print('in the bag')
        else:
            print('it wasn"t in the bag')
