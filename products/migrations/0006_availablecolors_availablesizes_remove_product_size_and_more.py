# Generated by Django 4.2.2 on 2023-07-21 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_has_sizes_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.availablecolors'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.availablesizes'),
        ),
    ]
