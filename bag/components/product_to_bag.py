from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product


class ProductToBagView(UnicornView):

    bag = None

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def add_item_to_bag(self, product_id):

        product = get_object_or_404(Product, id=1)

        bag = self.request.session.get('bag', {})
        bag[product_id] = 1
        self.call('rotate')
        # self.parent.add_to_bag(self, product_id)
        print(product)
        print(bag)
        print(self.parent, '123')
