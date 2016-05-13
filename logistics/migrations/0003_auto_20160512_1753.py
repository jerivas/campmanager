# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_auto_20150522_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallgroup',
            name='generation',
            field=models.PositiveIntegerField(choices=[(1, b'Jos\xc3\xadas 1'), (2, b'Jos\xc3\xadas 2'), (3, b'Freshmen'), (4, b'Sophomores'), (5, b'Juniors'), (6, b'Seniors'), (7, b'La Red'), (8, b'G180')], default=1, verbose_name='Generation'),
        ),
        migrations.AlterField(
            model_name='smallgroup',
            name='structure',
            field=models.CharField(blank=True, choices=[(b'preju', b'Preju'), (b'josias', b'Jos\xc3\xadas'), (b'lared', b'La Red'), (b'g180', b'G180')], max_length=16, verbose_name='Structure'),
        ),
    ]