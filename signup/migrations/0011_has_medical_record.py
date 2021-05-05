# Generated by Django 1.9.6 on 2016-06-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0010_enable_unaccent_extension"),
    ]

    operations = [
        migrations.AddField(
            model_name="camper",
            name="has_medical_record",
            field=models.BooleanField(
                default=False,
                help_text="This person has submitted their medical record",
                verbose_name="Medical record",
            ),
        ),
        migrations.AddField(
            model_name="counselor",
            name="has_medical_record",
            field=models.BooleanField(
                default=False,
                help_text="This person has submitted their medical record",
                verbose_name="Medical record",
            ),
        ),
        migrations.AddField(
            model_name="guest",
            name="has_medical_record",
            field=models.BooleanField(
                default=False,
                help_text="This person has submitted their medical record",
                verbose_name="Medical record",
            ),
        ),
    ]
