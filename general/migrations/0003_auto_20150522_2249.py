# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20150522_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='duration',
            field=models.CharField(help_text="Text describing the camp's duration", max_length=100, verbose_name='Duration'),
        ),
    ]
