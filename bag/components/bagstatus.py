from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404

import json


class BagstatusView(UnicornView):
    """
    Unicorn Component view that handles all the interractions with the bag session
    """

   ## bag['1']['L']['blue'] = 5 #qty


    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        self.quantity = 0
        return super().mount()

    def add_to_bag(self, product_id):
        self.quantity = 1
        self.bag[f'{product_id}'] = self.quantity
        self.request.session['bag'] = self.bag

    def remove_from_bag(self, product_id):
        self.bag.pop(str(product_id))
        self.request.session['bag'] = self.bag

