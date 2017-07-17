# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 04:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('signup', '0019_unique_with_site'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='camper',
            unique_together=set([('site', 'first_name', 'second_name', 'first_surname', 'second_surname')]),
        ),
        migrations.AlterUniqueTogether(
            name='counselor',
            unique_together=set([('site', 'first_name', 'second_name', 'first_surname', 'second_surname')]),
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('site', 'first_name', 'second_name', 'first_surname', 'second_surname')]),
        ),
        migrations.AlterUniqueTogether(
            name='parent',
            unique_together=set([('site', 'first_name', 'second_name', 'first_surname', 'second_surname')]),
        ),
    ]
