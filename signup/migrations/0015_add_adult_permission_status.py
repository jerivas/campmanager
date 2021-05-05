# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0014_reorder_structures"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camper",
            name="permission_status",
            field=models.IntegerField(
                choices=[
                    (
                        "Minors",
                        (
                            (0, "Pending Documentation"),
                            (1, "Ready to Print"),
                            (2, "Printed"),
                            (3, "Signed"),
                            (4, "Proofread"),
                            (5, "Special Case"),
                        ),
                    ),
                    ("Adults", ((6, "Pending ID"), (7, "Submitted ID"))),
                ],
                default=0,
                verbose_name="Permission Status",
            ),
        ),
    ]
