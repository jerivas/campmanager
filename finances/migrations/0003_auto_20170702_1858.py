# Generated by Django 1.10.7 on 2017-07-03 00:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finances", "0002_add_site_support"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Date"
            ),
        ),
    ]
