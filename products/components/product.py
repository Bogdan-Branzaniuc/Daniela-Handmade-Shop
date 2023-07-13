from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product


class ProductView(UnicornView):

    product = None
    bagtest = {}

    def mount(self, *args, **kwargs):
        self.product = get_object_or_404(Product, id=1)
        self.bagtest = self.request.session.get('bag', {})
        return super().mount()

    def product_in_bag(self):
        self.bagtest = self.request.session.get('bag', {})
