# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='end',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='start',
        ),
        migrations.AddField(
            model_name='camp',
            name='duration',
            field=models.CharField(default='from A to B', help_text="Text describing thecamp's duration", max_length=100, verbose_name='Duration'),
            preserve_default=False,
        ),
    ]
