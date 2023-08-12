from django.contrib import admin
from .models import Product, Category, AvailableColor, AvailableSize

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
admin.site.register(AvailableColor, AvailableColorsAdmin)
admin.site.register(AvailableSize, AvailableSizesAdmin)
