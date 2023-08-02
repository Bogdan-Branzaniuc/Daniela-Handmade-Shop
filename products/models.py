from django.db import models
from colorfield.fields import ColorField
from django.utils.html import format_html
from cloudinary.models import CloudinaryField

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class AvailableColors(models.Model):
    name_EN = models.CharField(max_length=100, unique=True, null=True)
    hexcolor = ColorField(max_length=7, default="#ffffff")

    def colored_name(self):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.hexcolor,
            self.name_EN,
        )

    def __str__(self):
        return self.name_EN

class AvailableSizes(models.Model):
    size = models.CharField(max_length=3, unique=True)
    expressed_in = models.CharField(
        max_length=9,
        choices=(('infants', 'infants'), ('standard', 'standard'), ('universal', 'universal')),
        default='standard')
    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = CloudinaryField(
        use_filename=True,
        unique_filename=False,
        folder='daniela_handmade/products',
        null=True,
        blank=True,
    )
    # Cloudinary image
    colors = models.ManyToManyField(
        'AvailableColors')
    sizes = models.ManyToManyField(
        'AvailableSizes')

    def __str__(self):
        return self.name


# class ProductRotation(models.Model):
#     name = models.OneToOneField(
#         Product,
#         on_delete=models.PROTECT,
#         primary_key=True,
#     )
#     img1 =
