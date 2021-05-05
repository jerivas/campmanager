# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SmallGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(unique=True, max_length=32, verbose_name="Title"),
                ),
                (
                    "generation",
                    models.PositiveIntegerField(
                        default=1,
                        max_length=1,
                        verbose_name="Generation",
                        choices=[
                            (1, "Josías 1"),
                            (2, "Josías 2"),
                            (3, "Freshmen"),
                            (4, "Sophomores"),
                            (5, "Juniors"),
                            (6, "Seniors"),
                        ],
                    ),
                ),
                (
                    "structure",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Structure",
                        choices=[("preju", "Preju"), ("josias", "Josías")],
                    ),
                ),
                (
                    "cabin",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Cabin",
                        choices=[
                            ("agape1", "Ágape 1"),
                            ("agape2", "Ágape 2"),
                            ("agape3", "Ágape 3"),
                            ("agape4", "Ágape 4"),
                            ("alfa", "Alfa"),
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("armenia", "Armenia"),
                            ("belen", "Belén"),
                            ("ebal", "Ebal"),
                            ("gerizim", "Gerizim"),
                            ("horeb1", "Horeb 1"),
                            ("horeb2", "Horeb 2"),
                            ("huespedes1", "Huéspedes 1"),
                            ("huespedes2", "Huéspedes 2"),
                            ("huespedes3", "Huéspedes 3"),
                            ("juda", "Judá"),
                            ("koinonia1", "Koinonía 1"),
                            ("koinonia2", "Koinonía 2"),
                            ("koinonia3", "Koinonía 3"),
                            ("koinonia4", "Koinonía 4"),
                            ("moa", "Moa"),
                            ("moria", "Moria"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("nueva3", "Nueva 3"),
                            ("nueva4", "Nueva 4"),
                            ("omega", "Omega"),
                            ("pastorales", "Pastorales"),
                            ("peniel", "Peniel"),
                            ("sinai", "Sinaí"),
                        ],
                    ),
                ),
                (
                    "bus",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Bus",
                        choices=[
                            ("1", "Bus 1"),
                            ("2", "Bus 2"),
                            ("3", "Bus 3"),
                            ("4", "Bus 4"),
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["generation"],
                "verbose_name": "Small Group",
                "verbose_name_plural": "Small Groups",
                "permissions": (
                    ("view_reports", "View Reports"),
                    ("attendant_report", "Attendant Report"),
                ),
            },
        ),
    ]
