
# pip install crispy
# pip3 install --user django-crispy-forms
# pip3 install django-crispy-forms
# pip install Pillow

# python3 manage.py runserver
# write 'python3 manage.py createsuperuser ' to check admin backend database - you create a new admin
    # then you follow the instructions, in particular, you enter the username 
    # "bonbongadmin" is a new superadmin (password is 111222333aA!)
    # then you login on http://127.0.0.1:8000/admin/ with your details and then you'd see the stuff
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
