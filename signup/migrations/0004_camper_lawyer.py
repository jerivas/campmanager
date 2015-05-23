# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        ('signup', '0003_remove_camper_lawyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='lawyer',
            field=models.ForeignKey(verbose_name='Assigned Lawyer', blank=True, to='general.Lawyer', null=True),
        ),
    ]
