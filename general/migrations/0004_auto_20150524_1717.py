# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0003_auto_20150522_2249"),
    ]

    operations = [
        migrations.AddField(
            model_name="camp",
            name="fine",
            field=models.DecimalField(
                default=3, verbose_name="Fine", max_digits=5, decimal_places=2
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="camp",
            name="price",
            field=models.DecimalField(
                default=75, verbose_name="Price", max_digits=5, decimal_places=2
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="camp",
            name="signup_fee",
            field=models.DecimalField(
                default=5, verbose_name="Signup fee", max_digits=5, decimal_places=2
            ),
            preserve_default=False,
        ),
    ]
