# Generated by Django 4.2.2 on 2023-07-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_availablesizes_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablesizes',
            name='expressed_in',
            field=models.CharField(choices=[('infants', 'infants'), ('standard', 'standard'), ('universal', 'universal')], default='standard', max_length=9),
        ),
    ]
