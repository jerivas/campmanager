# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('signup', '0018_add_site_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receipt_id',
            field=models.PositiveIntegerField(verbose_name='Receipt ID'),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([('site', 'receipt_id')]),
        ),
    ]