# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0004_auto_20150524_1717"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chaperone",
            name="occupation",
            field=models.CharField(
                max_length=99, verbose_name="Occupation", blank=True
            ),
        ),
    ]
