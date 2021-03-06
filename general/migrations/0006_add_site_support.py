# Generated by Django 1.10.7 on 2017-06-25 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("general", "0005_auto_20150704_1310"),
    ]

    operations = [
        migrations.AddField(
            model_name="camp",
            name="site",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="sites.Site",
                verbose_name="site",
            ),
            preserve_default=False,
        ),
    ]
