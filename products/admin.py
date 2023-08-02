from django.contrib import admin
from .models import Product, Category, AvailableColors, AvailableSizes

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'product_image',
    )

    filter_horizontal = ('colors', 'sizes')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class AvailableColorsAdmin(admin.ModelAdmin):
    list_display = ('name_EN', 'hexcolor', 'colored_name')

class AvailableSizesAdmin(admin.ModelAdmin):
    list_display = (
        'size',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AvailableColors, AvailableColorsAdmin)
admin.site.register(AvailableSizes, AvailableSizesAdmin)
