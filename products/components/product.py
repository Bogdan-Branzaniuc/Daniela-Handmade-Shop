from django_unicorn.components import UnicornView
from products.models import Product

class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    comp_bag_keys = []
    comp_sizes = []
    comp_colors = []
    sellected = None

    def mount(self, *args, **kwargs):
        self.comp_bag_keys = [int(id) for id in self.request.session.get('bag', {})]
        self.comp_sizes = ['S', 'M']
        self.comp_colors = ['red']
        return super().mount()

    def add_to_bag(self, product_id):
        if product_id not in self.comp_bag_keys:
            self.comp_bag_keys.append(product_id)

    def remove_from_bag(self, product_id):
        self.products = Product.objects.all()
        if product_id in self.comp_bag_keys:
            self.comp_bag_keys.remove(product_id)

    def sellect_color(self, sellection):
        self.sellected = sellection
        print(self.sellected)