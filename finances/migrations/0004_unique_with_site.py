# Generated by Django 1.11.3 on 2017-07-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("finances", "0003_auto_20170702_1858"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_id",
            field=models.CharField(
                blank=True, max_length=16, verbose_name="Transaction ID"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="transaction",
            unique_together={("site", "transaction_id")},
        ),
    ]
