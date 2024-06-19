# vercel_handler.py

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module based on environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passwor_manager.settings')

# Initialize Django application
django_application = get_wsgi_application()

# This function will be called by Vercel to handle incoming requests
def handler(event, context):
    # Pass the request to Django application
    return django_application(event, context)
