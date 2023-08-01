import os
from django.core.management import execute_from_command_line
import sys
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daniela_handmade.settings')
settings.DEBUG = True


if __name__ == '__main__':
    args = ['manage.py', 'runserver']
    execute_from_command_line(args)
