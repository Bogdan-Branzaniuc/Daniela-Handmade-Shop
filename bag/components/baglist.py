from django_unicorn.components import UnicornView
import json


class BaglistView(UnicornView):

    user_bag = None
    grand_total = 0

    def mount(self, *args, **kwargs):
        self.user_bag = self.request.session.get('bag', {})
        return super().mount()
