# Generated by Django 4.2.4 on 2023-08-12 10:24

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_availablesizes_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_EN', models.CharField(max_length=100, null=True, unique=True)),
                ('hexcolor', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=7, samples=None)),
            ],
        ),
        migrations.RenameModel(
            old_name='AvailableSizes',
            new_name='AvailableSize',
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='products.availablecolor'),
        ),
    ]