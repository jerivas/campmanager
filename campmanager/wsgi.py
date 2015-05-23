import os
import sys

project_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = project_dir.rsplit("/", 1)[0]
sys.path.extend([project_dir, parent_dir])
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
