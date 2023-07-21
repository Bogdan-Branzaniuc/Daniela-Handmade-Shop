from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404
import time

import json


class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def add_to_bag(self, product_id, size, color, qty):
        product_id = str(product_id)
        if product_id in self.bag.keys():
            if size in self.bag[product_id].keys():
                    self.bag[product_id][size][color] = qty
            else:
                self.bag[product_id][size] = {color: qty}
        else:
            self.bag[product_id] = {size: {color: qty}}

        self.request.session['bag'] = self.bag
        print(self.bag)

    def remove_from_bag(self, product_id, size, color):
        product_id = str(product_id)
        if product_id in self.bag.keys():
            if size in self.bag[product_id].keys():
                if color in self.bag[product_id][size].keys():
                    self.bag[product_id][size].pop(color)

        self.request.session['bag'] = self.bag
        print(self.bag)

