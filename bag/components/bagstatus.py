from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404

import json


class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def add_to_bag(self, product_id, size, color, qty):
        self.bag[f'{product_id}'] = {size: {color: qty}}
        self.request.session['bag'] = self.bag

    def remove_from_bag(self, product_id):
        self.bag.pop(str(product_id))
        self.request.session['bag'] = self.bag

