# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=75, verbose_name='Title')),
                ('destination', models.CharField(help_text='The Republic of...', max_length=75, verbose_name='Destination')),
                ('start', models.DateField(verbose_name='Start date')),
                ('end', models.DateField(verbose_name='End date')),
                ('permission_timestamp', models.DateTimeField(help_text='The date and time when the permissions are signed', verbose_name='Permission timestamp')),
                ('permission_location', models.CharField(help_text='The location where the permission are signed', max_length=75, verbose_name='Permission location')),
            ],
            options={
                'verbose_name': 'Camp',
            },
        ),
        migrations.CreateModel(
            name='Chaperone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[('m', 'Male'), ('f', 'Female')])),
                ('birth_date', models.DateTimeField(help_text='The format is YYYY-MM-DD and 24 hour time.', null=True, verbose_name='Birth Date', blank=True)),
                ('state', models.CharField(blank=True, choices=[('ahu', 'Ahuachapán'), ('cab', 'Cabañas'), ('cha', 'Chalatenango'), ('cus', 'Cuscatlán'), ('lal', 'La Libertad'), ('lap', 'La Paz'), ('lau', 'La Unión'), ('mor', 'Morazán'), ('saa', 'Santa Ana'), ('sam', 'San Miguel'), ('sas', 'San Salvador'), ('sav', 'San Vicente'), ('son', 'Sonsonate'), ('usu', 'Usulután')], max_length=3, verbose_name='State')),
                ('province', models.CharField(max_length=32, verbose_name='Province', blank=True)),
                ('occupation', models.CharField(max_length=32, verbose_name='Occupation', blank=True)),
                ('gov_id', models.CharField(max_length=10, verbose_name='ID Number', validators=[django.core.validators.RegexValidator(regex='^\\d{8}-\\d$', message='Invalid Government ID')])),
                ('camp', models.OneToOneField(verbose_name='Camp', to='general.Camp')),
            ],
            options={
                'verbose_name': 'Chaperone',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[('m', 'Male'), ('f', 'Female')])),
                ('camp', models.ForeignKey(verbose_name='Camp', to='general.Camp')),
            ],
            options={
                'verbose_name': 'Lawyer',
                'verbose_name_plural': 'Lawyers',
            },
        ),
    ]
