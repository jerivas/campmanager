# Generated by Django 1.11.3 on 2017-07-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("logistics", "0007_add_site_support"),
    ]

    operations = [
        migrations.AlterField(
            model_name="smallgroup",
            name="title",
            field=models.CharField(max_length=32, verbose_name="Title"),
        ),
        migrations.AlterUniqueTogether(
            name="smallgroup",
            unique_together={("site", "title")},
        ),
    ]
