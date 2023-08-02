# Generated by Django 4.2.2 on 2023-07-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_product_colors_remove_product_sizes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='products.availablecolors'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='products.availablesizes'),
        ),
    ]