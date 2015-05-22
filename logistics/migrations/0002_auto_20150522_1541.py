# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallgroup',
            name='generation',
            field=models.PositiveIntegerField(default=1, verbose_name='Generation', choices=[(1, b'Jos\xc3\xadas 1'), (2, b'Jos\xc3\xadas 2'), (3, b'Freshmen'), (4, b'Sophomores'), (5, b'Juniors'), (6, b'Seniors')]),
        ),
    ]
