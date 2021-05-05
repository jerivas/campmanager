# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):
    """
    Enable Postgre's unaccent extension to support unaccent lookups.
    https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/lookups/#unaccent
    Please bear in mind that the DB user must have superuser rights to
    create extensions. You can enable it with:
        postgres# ALTER ROLE <user_name> SUPERUSER;

    And after the installation you can roll back the privilege:
        postgres# ALTER ROLE <user_name> NOSUPERUSER;
    """

    dependencies = [
        ("signup", "0009_auto_20160512_1753"),
    ]

    operations = [UnaccentExtension()]
