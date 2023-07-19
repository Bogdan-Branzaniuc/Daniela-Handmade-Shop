from django.core.management import execute_from_command_line
import sys


if __name__ == '__main__':
    sys.argv.append('runserver')
    sys.argv.append('127.0.0.1:8000')  # Specify the desired host and port
    execute_from_command_line(sys.argv)
