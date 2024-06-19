# vercel_handler.py

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module based on environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passwor_manager.settings')

# Initialize Django application
django_application = get_wsgi_application()

# This function will be called by Vercel to handle incoming requests
def handler(event, context):
    # Pass the request to Django application
    return django_application(event, context)
