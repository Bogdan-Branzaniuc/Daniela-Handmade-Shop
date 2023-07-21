# Generated by Django 4.2.2 on 2023-07-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_availablesizes_expressed_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, to='products.availablecolors'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, null=True, to='products.availablesizes'),
        ),
    ]
