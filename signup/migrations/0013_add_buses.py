# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0012_payment_receipt_id_to_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camper',
            name='bus',
            field=models.CharField(blank=True, choices=[('1', 'Bus 1'), ('2', 'Bus 2'), ('3', 'Bus 3'), ('4', 'Bus 4'), ('5', 'Bus 5'), ('6', 'Bus 6'), ('7', 'Bus 7')], max_length=16, verbose_name='Bus'),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='bus',
            field=models.CharField(blank=True, choices=[('1', 'Bus 1'), ('2', 'Bus 2'), ('3', 'Bus 3'), ('4', 'Bus 4'), ('5', 'Bus 5'), ('6', 'Bus 6'), ('7', 'Bus 7')], max_length=16, verbose_name='Bus'),
        ),
    ]
