from django_unicorn.components import UnicornView


class ItemInBagView(UnicornView):
    """
    Unicorn Component view that handles the user interactions with the bag
    """
    editing = None
    def mount(self, *args, **kwargs):
        self.editing = 'false'
        self.user_bag = self.request.session.get('bag', {})
        self.editig_bag_item_mode()

        return super().mount()

    def editing_product(self):
        self.editing = 'true'
        self.editig_bag_item_mode()


    def submit_changes(self):
        self.editing = 'false'
        self.editig_bag_item_mode()

    def editig_bag_item_mode(self):
        if self.editing == 'true':
            self.call('enableEditingMode', self.item_index)
        elif self.editing == 'false':
            self.call('disableEditingMode', self.item_index)