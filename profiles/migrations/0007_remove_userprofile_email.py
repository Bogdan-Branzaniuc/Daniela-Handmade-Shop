# Generated by Django 4.2.4 on 2023-08-12 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
