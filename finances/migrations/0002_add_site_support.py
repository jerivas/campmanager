# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-25 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='site',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
    ]
