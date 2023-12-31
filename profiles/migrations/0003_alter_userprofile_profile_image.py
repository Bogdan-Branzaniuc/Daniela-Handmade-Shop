# Generated by Django 4.2.2 on 2023-07-04 20:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
