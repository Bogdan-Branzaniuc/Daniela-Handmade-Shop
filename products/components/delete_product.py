from django_unicorn.components import UnicornView
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib import messages


class DeleteProductView(UnicornView):

    product = None
    soft_deleted_product = None

    def mount(self):
        self.soft_deleted_product = False

    def soft_delete_this_product(self):
        self.soft_deleted_product = True

    def restore_product(self):
        self.soft_deleted_product = False

    def delete_product(self):
        if self.soft_deleted_product:
            product = get_object_or_404(Product, pk=self.product.id)
            product.delete()
            messages.success(self.request, f"Successfully deleted {self.product.name}")
            self.call('pageReload')
