from django_unicorn.components import UnicornView
from django.contrib import messages

class ItemInBagView(UnicornView):
    """
    Unicorn Component view that handles the user interactions with the bag
    """
    editing = False
    component_quantity = None
    original_state_size = None
    original_state_color = None
    selected_size = None
    selected_color = None
    soft_deleted = False
    deleted = False
    product_image_url = None
    bag = dict

    def mount(self, *args, **kwargs):
        self.bag = self.request.session.get('bag', {})
        self.original_state_size = self.selected_size = self.item['size']
        self.original_state_color = self.selected_color = self.item['color'].name_EN
        self.component_quantity = self.item['quantity']
        self.update_selections_focus_buttons()
        self.product_image_url = self.product.product_image.url
        return super().mount()

    def editing_product(self):
        """
        switches to editing state
        """
        self.bag = self.request.session.get('bag', {})
        self.editing = True
        self.update_selections_focus_buttons()

    def adjust_bag(self):
        """
        code to adjust the bag, when adding quantity or editing,
        if same configuration of color and size is present, combines their quantities
        """
        bag = self.request.session.get('bag', {})
        o_size = self.original_state_size
        s_size = self.selected_size
        o_color = self.original_state_color
        s_color = self.selected_color
        p_id = self.item['item_id']
        qty = self.component_quantity
        combined = False

        if qty > 0:
            if s_size != o_size:
                bag[p_id][o_size].pop(o_color)
                if bag[p_id][o_size] == {}:
                    bag[p_id].pop(o_size)
                if s_size in bag[p_id].keys():
                    if s_color in bag[p_id][s_size].keys():
                        qty += bag[p_id][s_size][s_color]
                        bag[p_id][s_size][s_color] = qty
                        combined = True
                    else:
                        bag[p_id][s_size][s_color] = qty
                else:
                    bag[p_id][s_size] = {s_color: qty}
            else:
                if s_color != o_color:
                    bag[p_id][s_size].pop(o_color)
                    if s_color in bag[p_id][s_size].keys():
                        qty += bag[p_id][s_size][s_color]
                        bag[p_id][s_size][s_color] = qty
                        combined = True
                    else:
                        bag[p_id][s_size][s_color] = qty
                else:
                    bag[p_id][s_size][s_color] = qty
            self.request.session['bag'] = bag
        else:
            self.soft_deleted = True

        self.item['color'] = self.product.colors.get(name_EN=s_color)
        self.item['size'] = self.product.sizes.get(size=s_size)
        self.original_state_size = s_size
        self.original_state_color = s_color
        self.selected_color = s_color
        self.selected_size = s_size
        self.component_quantity = qty
        self.editing = False
        self.call('updateBagstatus')
        if combined:
            self.call('pageReload')
            messages.add_message(self.request, messages.INFO, "the same product was already in your bag, We combined the quantities for you")

    def soft_removal_from_bag(self):
        """
        Give the user the chance to add the item back, or delete it for good.
        """
        self.bag = self.request.session.get('bag', {})
        self.soft_deleted = True
        self.editing = False

    def add_item_back(self):
        self.bag = self.request.session.get('bag', {})
        self.soft_deleted = False
        self.editing = False

    def remove_bag_item(self):
        self.bag = self.request.session.get('bag', {})
        product_id = self.item['item_id']
        if product_id in self.bag.keys():
            if self.selected_size in self.bag[product_id].keys():
                if self.selected_color in self.bag[product_id][self.selected_size].keys():
                    self.bag[product_id][self.selected_size].pop(self.selected_color)
                    if self.bag[product_id][self.selected_size] == {}:
                        self.bag[product_id].pop(self.selected_size)
                    if self.bag[product_id] == {}:
                        self.bag.pop(product_id)

        self.request.session['bag'] = self.bag
        self.deleted = True
        self.call('updateBagstatus')

    def increment_component_quantity(self):
        """
        increments component quantity
        """
        self.bag = self.request.session.get('bag', {})
        self.component_quantity += 1
        self.update_selections_focus_buttons()

    def decrement_component_quantity(self):
        """
        decrements component quantity
        """
        self.bag = self.request.session.get('bag', {})
        if self.component_quantity > 0:
            self.component_quantity -= 1
        else:
            self.component_quantity = 0
        self.update_selections_focus_buttons()

    def update_selections_focus_buttons(self):
        """
        code that transfers selected options and focused buttons from this view to product_component_selectors.js file
        """
        self.call('setSelectedSizeColorQty', self.selected_size, self.selected_color, self.component_quantity)
        self.call('focusProductButtons', f"button-{self.selected_color}-{self.item_index}", self.selected_color)
        self.call('focusProductButtons', f"button-{self.selected_size}-{self.item_index}", self.selected_size)

    def select_size_or_color(self, selection, size_or_color):
        """
        calls js product_component_selector.js functions to set component properties
        """
        self.bag = self.request.session.get('bag', {})
        if size_or_color == 'color':
            self.selected_color = selection
        elif size_or_color == 'size':
            self.selected_size = selection
        self.update_selections_focus_buttons()
