#!/usr/bin/env python
import os
import sys

# Add the site ID CLI arg to the environment, which allows for the site
# used in any site related queries to be manually set for management commands.
for i, arg in enumerate(sys.argv):
    if arg.startswith("--site"):
        try:
            # For the --site=ID syntax
            os.environ["DJANGO_SITE_ID"] = arg.split("=")[1]
        except IndexError:
            # For the --site ID syntax
            os.environ["DJANGO_SITE_ID"] = sys.argv.pop(i + 1)
        sys.argv.pop(i)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "campmanager.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
