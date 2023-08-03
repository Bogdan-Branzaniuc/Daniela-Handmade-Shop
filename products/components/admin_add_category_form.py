from django_unicorn.components import UnicornView
from products.models import Category
from django.contrib import messages

class AdminAddCategoryFormView(UnicornView):

    categories = None
    category = ''
    soft_deleted_categories = None

    def mount(self):
        self.categories = Category.objects.all()
        self.soft_deleted_categories = []

    def add_category(self):
        if not Category.objects.filter(name=self.category).exists():
            Category.objects.create(
                name=self.category,
                friendly_name=self.category
            )
        else:
            messages.error(self.request, f'{self.name} is already in the available colors')
        self.call('pageReload')

    def soft_delete(self, category):
        self.soft_deleted_categories.append(category)

    def restore_category(self, category):
        self.soft_deleted_categories.remove(category)

    def perma_delete_category(self, category):
        Category.objects.get(name=category).delete()
        self.soft_deleted_categories.remove(category)
        self.call('pageReload')
        messages.success(self.request, f"Successfully deleted {category} from categories")