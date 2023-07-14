from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product


class ProductView(UnicornView):

    product = None

    def mount(self, *args, **kwargs):
        self.product = get_object_or_404(Product, id=1)
        
        return super().mount()

    def product_in_bag(self, product_id):
        pass
