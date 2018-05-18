# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(unique=True, max_length=16, verbose_name='Transaction ID', blank=True)),
                ('transaction_type', models.CharField(max_length=16, verbose_name='Type', choices=[('income', 'Income'), ('egress', 'Egress')])),
                ('transaction_date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=6, decimal_places=2)),
                ('origin', models.CharField(max_length=128, verbose_name='Origin', blank=True)),
                ('destination', models.CharField(max_length=128, verbose_name='Destination', blank=True)),
            ],
            options={
                'ordering': ['-transaction_id'],
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'permissions': (('view_reports', 'View Reports'),),
            },
        ),
    ]
