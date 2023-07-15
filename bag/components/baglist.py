from django_unicorn.components import UnicornView
import json


class BaglistView(UnicornView):
    """
    Unicorn Component view that handles only the user interactions with the bag 
    """

    user_bag = None

    def mount(self, *args, **kwargs):
        self.user_bag = self.request.session.get('bag', {})
        return super().mount()
