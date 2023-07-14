from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404

import json


class BagstatusView(UnicornView):

    bag = None

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        return super().mount()

    def add_to_bag(self, product_id):

        bag = self.request.session.get('bag', {})
        bag[product_id] = 1
        self.request.session['bag'] = bag
