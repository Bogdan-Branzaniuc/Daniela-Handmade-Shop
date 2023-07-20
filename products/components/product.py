from django_unicorn.components import UnicornView
from products.models import Product

class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    in_bag = None
    selected_color = 'red'
    selected_size = ''
    bag = {}
    def mount(self, *args, **kwargs):
        self.in_bag = False
        self.bag = self.request.session.get('bag', {})
        self.call('setSelectedColor', self.selected_color)
        if self.product.size == 'baby':
            self.selected_size = '2m'
        elif self.product.size == 'standard':
            self.selected_size = 'M'
        else:
            self.selected_size = 'U'
        self.call('setSelectedSize', self.selected_size)

        self.is_in_bag()

        return super().mount()

    def is_in_bag(self):
        str_id = str(self.product.id)
        self.bag = self.request.session.get('bag', {})
        if str_id in self.bag.keys():
            if self.selected_size in self.bag[str_id].keys():
                if self.selected_color in self.bag[str_id][self.selected_size].keys():
                    self.in_bag = True
                else:
                    self.in_bag = False
            else:
                self.in_bag = False
        else:
            self.in_bag = False
        print(str_id)
        print(self.selected_size)
        print(self.selected_color)
        print(self.in_bag)
        print(self.bag)
    def add_to_bag(self):
        self.call('setSelectedColor', self.selected_color)
        self.call('setSelectedSize', self.selected_size)
        self.in_bag = True
        print(self.product.id)
        print(self.selected_size)
        print(self.selected_color)

    def remove_from_bag(self):
        self.in_bag = False
        self.call('setSelectedColor', self.selected_color)
        self.call('setSelectedSize', self.selected_size)

    def select_color(self, selection):
        self.selected_color = selection
        self.call('setSelectedColor', self.selected_color)
        self.is_in_bag()

    def select_size(self, selection):
        self.selected_size = selection
        self.call('setSelectedSize', self.selected_size)
        self.is_in_bag()
