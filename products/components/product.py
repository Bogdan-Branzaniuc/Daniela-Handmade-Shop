from django_unicorn.components import UnicornView


class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    bag = {}
    in_bag = None
    component_quantity = None
    component_quantity_changed = None
    selected_color = ''
    selected_size = ''

    def mount(self, *args, **kwargs):
        self.in_bag = False
        self.component_quantity = 0
        self.component_quantity_changed = False
        self.bag = self.request.session.get('bag', {})
        self.selected_size = str(self.product.sizes.all()[0])
        self.selected_color = str(self.product.colors.all()[0])
        self.call('setSelectedColor', self.selected_color)
        self.call('setSelectedSize', self.selected_size)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.product.id}", self.selected_color)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.product.id}", self.selected_size)
        self.is_in_bag()
        print(self.component_quantity)
        return super().mount()

    def is_in_bag(self):
        """
        Sets the property in_bag to True or False by evaluating the bag stored in session
        in_bag property helps render the 'delete from bag' button in the product component template
        sets self.component_quantity according to the bag object in the current session
        """
        str_id = str(self.product.id)
        self.bag = self.request.session.get('bag', {})
        if str_id in self.bag.keys():
            if self.selected_size in self.bag[str_id].keys():
                if self.selected_color in self.bag[str_id][self.selected_size].keys():
                    self.component_quantity = self.bag[str_id][self.selected_size][self.selected_color]
                    self.in_bag = True
                else:
                    self.in_bag = False
            else:
                self.in_bag = False
        else:
            self.in_bag = False
    def add_to_bag(self):
        """
        sets in_bag to True for instantaneous rendering of the product component template
        calls js product_component_selector.js functions to set component properties
        """
        if self.component_quantity == 0:
            self.component_quantity = 1

        self.in_bag = True
        self.call('setSelectedColor', self.selected_color)
        self.call('setSelectedSize', self.selected_size)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.product.id}", self.selected_color)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.product.id}", self.selected_size)

    def remove_from_bag(self):
        """
        sets in_bag to False for instantaneous rendering of the product component template
        calls js product_component_selector.js functions to set component properties
        """
        self.in_bag = False
        self.component_quantity = 0
        self.call('setSelectedColor', self.selected_color)
        self.call('setSelectedSize', self.selected_size)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.product.id}", self.selected_color)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.product.id}", self.selected_size)

    def adjust_bag(self):
        self.component_quantity_changed = False
        print('adjusted')
    def select_size_or_color(self, selection, size_or_color):
        """
        calls js product_component_selector.js functions to set component properties
        """
        if size_or_color == 'color':
            self.selected_color = selection
            self.call('setSelectedColor', self.selected_color)
        elif size_or_color == 'size':
            self.selected_size = selection
            self.call('setSelectedSize', self.selected_size)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.product.id}", self.selected_color)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.product.id}", self.selected_size)


    def increment_component_quantity(self):
        print(self.component_quantity)
        self.component_quantity += 1
        self.component_quantity_changed = True
        self.call('setSelectedQuantity', self.component_quantity)

    def decrement_component_quantity(self):
        print(self.component_quantity)
        if self.component_quantity > 0:
            self.component_quantity -= 1
        else:
            self.component_quantity = 0
        self.component_quantity_changed = True
        self.call('setSelectedQuantity', self.component_quantity)
