# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmallGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=32, verbose_name='Title')),
                ('generation', models.PositiveIntegerField(default=1, max_length=1, verbose_name='Generation', choices=[(1, b'Jos\xc3\xadas 1'), (2, b'Jos\xc3\xadas 2'), (3, b'Freshmen'), (4, b'Sophomores'), (5, b'Juniors'), (6, b'Seniors')])),
                ('structure', models.CharField(blank=True, max_length=16, verbose_name='Structure', choices=[(b'preju', b'Preju'), (b'josias', b'Jos\xc3\xadas')])),
                ('cabin', models.CharField(blank=True, max_length=16, verbose_name='Cabin', choices=[(b'agape1', b'\xc3\x81gape 1'), (b'agape2', b'\xc3\x81gape 2'), (b'agape3', b'\xc3\x81gape 3'), (b'agape4', b'\xc3\x81gape 4'), (b'alfa', b'Alfa'), (b'anakaino1', b'Anakaino 1'), (b'anakaino2', b'Anakaino 2'), (b'anakaino3', b'Anakaino 3'), (b'anakaino4', b'Anakaino 4'), (b'armenia', b'Armenia'), (b'belen', b'Bel\xc3\xa9n'), (b'ebal', b'Ebal'), (b'gerizim', b'Gerizim'), (b'horeb1', b'Horeb 1'), (b'horeb2', b'Horeb 2'), (b'huespedes1', b'Hu\xc3\xa9spedes 1'), (b'huespedes2', b'Hu\xc3\xa9spedes 2'), (b'huespedes3', b'Hu\xc3\xa9spedes 3'), (b'juda', b'Jud\xc3\xa1'), (b'koinonia1', b'Koinon\xc3\xada 1'), (b'koinonia2', b'Koinon\xc3\xada 2'), (b'koinonia3', b'Koinon\xc3\xada 3'), (b'koinonia4', b'Koinon\xc3\xada 4'), (b'moab', b'Moab'), (b'moria', b'Moria'), (b'nueva1', b'Nueva 1'), (b'nueva2', b'Nueva 2'), (b'nueva3', b'Nueva 3'), (b'nueva4', b'Nueva 4'), (b'omega', b'Omega'), (b'pastorales', b'Pastorales'), (b'peniel', b'Peniel'), (b'sinai', b'Sina\xc3\xad')])),
                ('bus', models.CharField(blank=True, max_length=16, verbose_name='Bus', choices=[(b'1', b'Bus 1'), (b'2', b'Bus 2'), (b'3', b'Bus 3'), (b'4', b'Bus 4')])),
            ],
            options={
                'ordering': ['generation'],
                'verbose_name': 'Small Group',
                'verbose_name_plural': 'Small Groups',
                'permissions': (('view_reports', 'View Reports'), ('attendant_report', 'Attendant Report')),
            },
        ),
    ]
