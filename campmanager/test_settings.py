from campmanager.settings import *  # noqa

# Disable whitenoise to ignore static files errors
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Stop Django Dynamic Fixture from creating site records automatically
DDF_IGNORE_FIELDS = ["site"]
