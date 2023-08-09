from django_unicorn.components import UnicornView

class ProductView(UnicornView):
    """
    Unicorn Component view that handles user interactions with products
    """
    bag = None
    in_bag = None
    component_quantity = None
    component_quantity_changed = None
    selected_color = None
    selected_size = None
    product_image_url = None
    str_id = None
    show_detail = None
    selected_rgba = None


    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.update_selections_focus_buttons()
        self.is_in_bag()
        self.product_image_url = self.product.product_image.url
        self.str_id = str(self.product.id)
        self.show_detail = False

    def mount(self, *args, **kwargs):
        self.in_bag = False
        self.component_quantity = 0
        self.component_quantity_changed = False
        self.bag = self.request.session.get('bag', {})
        self.selected_size = str(self.product.sizes.all()[0])
        self.selected_color = str(self.product.colors.all()[0])
        self.selected_rgba = self.rgba_colors[self.selected_color]
        return super().mount()

    def toggle_detail(self):
        self.show_detail = True if not self.show_detail else False
        self.update_selections_focus_buttons()
        self.is_in_bag()

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
                    self.component_quantity = 0
            else:
                self.in_bag = False
        else:
            self.in_bag = False

    def update_selections_focus_buttons(self):
        """
        code that transfers selected options and focused buttons from this view to product_component_selectors.js file
        """
        self.call('setSelectedSizeColorQty', self.selected_size, self.selected_color, self.component_quantity)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.product.id}", self.selected_size)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.product.id}", self.selected_color)

    def add_to_bag(self):
        """
        sets in_bag to True for instantaneous rendering of the product component template
        calls js product_component_selector.js functions to send this component's view properties into JS that calls the bag component's view
        """
        self.bag = self.request.session.get('bag', {})
        if not self.component_quantity_changed:
            self.component_quantity += 1
        str_id = str(self.product.id)

        if str_id in self.bag.keys():
            if self.selected_size in self.bag[str_id].keys():
                self.bag[str_id][self.selected_size][self.selected_color] = self.component_quantity
            else:
                self.bag[str_id][self.selected_size] = {self.selected_color: self.component_quantity}
        else:
            self.bag[str_id] = {self.selected_size: {self.selected_color: self.component_quantity}}

        self.request.session['bag'] = self.bag

        self.in_bag = True
        self.component_quantity_changed = False
        self.update_selections_focus_buttons()

    def remove_from_bag(self):
        """
        sets in_bag to False for instantaneous rendering of the product component template
        calls js product_component_selector.js functions to send this component's view properties into JS that calls the bag component's view
        """
        product_id = str(self.product.id)
        if product_id in self.bag.keys():
            if self.selected_size in self.bag[product_id].keys():
                if self.selected_color in self.bag[product_id][self.selected_size].keys():
                    self.bag[product_id][self.selected_size].pop(self.selected_color)
                    if self.bag[product_id][self.selected_size] == {}:
                        self.bag[product_id].pop(self.selected_size)
                    if self.bag[product_id] == {}:
                        self.bag.pop(product_id)

        self.request.session['bag'] = self.bag

        self.in_bag = False
        self.component_quantity_changed = False
        self.component_quantity = 0
        self.update_selections_focus_buttons()

    def adjust_bag(self):
        self.component_quantity_changed = False
        if self.component_quantity > 0:
            self.component_quantity_changed = True
            self.add_to_bag()
            self.in_bag = True
        else:
            self.remove_from_bag()
            self.in_bag = False
        self.update_selections_focus_buttons()

    def select_size_or_color(self, selection, size_or_color):
        """
        calls js product_component_selector.js functions to set component properties
        """
        if size_or_color == 'color':
            self.selected_color = selection
        elif size_or_color == 'size':
            self.selected_size = selection
        self.is_in_bag()
        self.selected_rgba = self.rgba_colors[self.selected_color]
        self.update_selections_focus_buttons()


    def increment_component_quantity(self):
        self.component_quantity += 1
        self.component_quantity_changed = True
        self.update_selections_focus_buttons()

    def decrement_component_quantity(self):
        if self.component_quantity > 0:
            self.component_quantity -= 1
        else:
            self.component_quantity = 0
        self.component_quantity_changed = True
        self.update_selections_focus_buttons()