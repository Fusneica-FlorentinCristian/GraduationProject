import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GraduationProject.settings')
import django
django.setup()

from django.contrib.auth.models import User