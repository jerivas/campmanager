# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0006_auto_20150524_1732"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camper",
            name="permission_status",
            field=models.IntegerField(
                default=0,
                verbose_name="Permission Status",
                choices=[
                    (0, "Pending Documentation"),
                    (1, "Ready to Print"),
                    (2, "Printed"),
                    (3, "Signed"),
                    (4, "Proofread"),
                    (5, "Special Case"),
                ],
            ),
        ),
    ]
