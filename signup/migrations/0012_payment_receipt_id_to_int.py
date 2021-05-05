# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError, migrations, models, transaction


def id_to_int(apps, schema_editor):
    """
    Populate receipt_id_int with coerced values from receipt_id.
    """
    Payment = apps.get_model("signup", "Payment")
    for p in Payment.objects.all():
        try:
            with transaction.atomic():
                receipt_id = int(p.receipt_id)
                p.receipt_id_int = receipt_id
                p.receipt_id = "%s" % receipt_id  # Will trigger unique checks
                p.save()
        except (IntegrityError, ValueError):
            # Payments will be lost if they can't be coerced or are not unique
            p.delete()


class Migration(migrations.Migration):
    """
    Convert Payment.receipt_id from CharField to PositiveIntegerField.
    """

    dependencies = [
        ("signup", "0011_has_medical_record"),
    ]

    operations = [
        # Add the receipt_id_int as placeholder
        migrations.AddField(
            model_name="payment",
            name="receipt_id_int",
            field=models.PositiveIntegerField(null=True),
        ),
        # Populate receipt_id_int with values from receipt_id
        migrations.RunPython(id_to_int),
        # Delete the original receipt_id
        migrations.RemoveField(
            model_name="payment",
            name="receipt_id",
        ),
        # Rename receipt_id_int into receipt_id
        migrations.RenameField(
            model_name="payment", old_name="receipt_id_int", new_name="receipt_id"
        ),
        # Set the unique constraints to match models.py
        migrations.AlterField(
            model_name="payment",
            name="receipt_id",
            field=models.PositiveIntegerField(unique=True, verbose_name="Receipt ID"),
        ),
    ]
