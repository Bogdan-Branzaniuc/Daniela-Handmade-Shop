from django_unicorn.components import UnicornView
from products.models import Category


class NavCategoriesView(UnicornView):

    categories = None

    def mount(self):
        self.categories = Category.objects.all()

