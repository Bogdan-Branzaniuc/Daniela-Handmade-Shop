# Generated by Django 4.2.2 on 2023-07-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_productimages_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('standard', 'standard'), ('baby', 'baby'), ('universal', 'universal')], default='standard', max_length=50, null=True),
        ),
    ]
