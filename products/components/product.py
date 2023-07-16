from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product


class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    products = None
    bag = None
    bag_keys = None

    def mount(self, *args, **kwargs):
        self.products = Product.objects.all()
        self.bag = self.request.session.get('bag', {})
        self.bag_keys = list(int(key) for key in self.bag.keys())
        return super().mount()

    def ad_or_remove_from_bag(self):
        self.bag = self.request.session.get('bag', {})
        self.bag_keys = list(int(key) for key in self.bag.keys())

