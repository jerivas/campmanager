# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0013_add_buses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camper',
            name='structure',
            field=models.CharField(blank=True, choices=[('josias', 'Josías'), ('preju', 'Preju'), ('lared', 'La Red'), ('g180', 'G180')], max_length=16, verbose_name='Structure'),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='structure',
            field=models.CharField(blank=True, choices=[('josias', 'Josías'), ('preju', 'Preju'), ('lared', 'La Red'), ('g180', 'G180')], max_length=16, verbose_name='Structure'),
        ),
    ]
