# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0007_auto_20150531_1902"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camper",
            name="occupation",
            field=models.CharField(
                max_length=99, verbose_name="Occupation", blank=True
            ),
        ),
        migrations.AlterField(
            model_name="parent",
            name="occupation",
            field=models.CharField(
                max_length=99, verbose_name="Occupation", blank=True
            ),
        ),
    ]
