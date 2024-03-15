
import os
import sys
from pathlib import Path

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_agenda.settings'
settings.USE_TZ = False

django.setup()
if __name__ == '__main__':
    from contact.models import Category, Contact
    Contact.objects.all().delete()
    Category.objects.all().delete()
