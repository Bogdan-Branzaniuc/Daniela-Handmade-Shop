from django_unicorn.components import UnicornView
from django.shortcuts import render, get_object_or_404
from products.models import Product

class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    products = Product.objects.all()
    comp_bag_keys = []


    def mount(self, *args, **kwargs):
        self.products = Product.objects.all()
        self.bag = self.request.session.get('bag', {})
        self.comp_bag_keys = [int(id) for id in self.request.session.get('bag', {})]
        return super().mount()

    def add_to_bag(self, product_id):
        self.products = Product.objects.all()
        if product_id not in self.comp_bag_keys:
            self.comp_bag_keys.append(product_id)
        print(self.comp_bag_keys)

    def remove_from_bag(self, product_id):
        print(2)
        self.products = Product.objects.all()
        if product_id in self.comp_bag_keys:
            self.comp_bag_keys.remove(product_id)
