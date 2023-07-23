from django_unicorn.components import UnicornView


class ItemInBagView(UnicornView):
    """
    Unicorn Component view that handles the user interactions with the bag
    """
    editing = None


    def mount(self, *args, **kwargs):
        self.editing = False
        self.user_bag = self.request.session.get('bag', {})
        return super().mount()

    def editing_product(self):
        self.editing = True
        print(self.editing)

    def submit_changes(self):
        self.editing = False
