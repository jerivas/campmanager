# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camper',
            name='generation',
            field=models.PositiveIntegerField(verbose_name='Generation', choices=[(1, 'Josías 1'), (2, 'Josías 2'), (3, 'Freshmen'), (4, 'Sophomores'), (5, 'Juniors'), (6, 'Seniors')]),
        ),
        migrations.AlterField(
            model_name='camper',
            name='permission_status',
            field=models.IntegerField(default=0, verbose_name='Permission Status', choices=[(0, 'Incomplete Documentation'), (1, 'Ready to Print'), (2, 'Printed'), (3, 'Signed'), (4, 'Special Case')]),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='generation',
            field=models.PositiveIntegerField(verbose_name='Generation', choices=[(1, 'Josías 1'), (2, 'Josías 2'), (3, 'Freshmen'), (4, 'Sophomores'), (5, 'Juniors'), (6, 'Seniors')]),
        ),
    ]
