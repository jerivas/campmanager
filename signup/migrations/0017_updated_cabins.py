# Generated by Django 1.9.6 on 2016-07-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0016_counselor_has_gov_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camper",
            name="cabin",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Sector Norte",
                        (
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("koinonia1", "Koinonia 1"),
                            ("koinonia2", "Koinonia 2"),
                            ("koinonia3", "Koinonia 3"),
                            ("koinonia4", "Koinonia 4"),
                            ("alfa", "Alfa"),
                            ("omega", "Omega"),
                            ("oasis", "Oasis"),
                        ),
                    ),
                    (
                        "Sector Centro",
                        (
                            ("agape1", "Ágape 1"),
                            ("agape2", "Ágape 2"),
                            ("agape3", "Ágape 3"),
                            ("agape4", "Ágape 4"),
                            ("huespedes1", "Huespedes 1"),
                            ("huespedes2", "Huespedes 2"),
                            ("huespedes3", "Huespedes 3"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("pastoral", "Pastoral"),
                        ),
                    ),
                    (
                        "Sector Campo",
                        (
                            ("moab", "Moab"),
                            ("esmirna", "Esmirna"),
                            ("efeso", "Éfeso"),
                            ("juda", "Judá"),
                            ("belen", "Belén"),
                            ("sinai", "Sinaí"),
                            ("gerisim", "Gerisim"),
                        ),
                    ),
                    (
                        "Sector Lago",
                        (
                            ("armenia", "Armenia"),
                            ("horeb", "Horeb"),
                            ("filadelfia", "Filadelfia"),
                            ("ebal", "Ebal"),
                            ("peniel", "Peniel"),
                            ("moria", "Moria"),
                        ),
                    ),
                ],
                max_length=16,
                verbose_name="Cabin",
            ),
        ),
        migrations.AlterField(
            model_name="counselor",
            name="cabin",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Sector Norte",
                        (
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("koinonia1", "Koinonia 1"),
                            ("koinonia2", "Koinonia 2"),
                            ("koinonia3", "Koinonia 3"),
                            ("koinonia4", "Koinonia 4"),
                            ("alfa", "Alfa"),
                            ("omega", "Omega"),
                            ("oasis", "Oasis"),
                        ),
                    ),
                    (
                        "Sector Centro",
                        (
                            ("agape1", "Ágape 1"),
                            ("agape2", "Ágape 2"),
                            ("agape3", "Ágape 3"),
                            ("agape4", "Ágape 4"),
                            ("huespedes1", "Huespedes 1"),
                            ("huespedes2", "Huespedes 2"),
                            ("huespedes3", "Huespedes 3"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("pastoral", "Pastoral"),
                        ),
                    ),
                    (
                        "Sector Campo",
                        (
                            ("moab", "Moab"),
                            ("esmirna", "Esmirna"),
                            ("efeso", "Éfeso"),
                            ("juda", "Judá"),
                            ("belen", "Belén"),
                            ("sinai", "Sinaí"),
                            ("gerisim", "Gerisim"),
                        ),
                    ),
                    (
                        "Sector Lago",
                        (
                            ("armenia", "Armenia"),
                            ("horeb", "Horeb"),
                            ("filadelfia", "Filadelfia"),
                            ("ebal", "Ebal"),
                            ("peniel", "Peniel"),
                            ("moria", "Moria"),
                        ),
                    ),
                ],
                max_length=16,
                verbose_name="Cabin",
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="cabin",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Sector Norte",
                        (
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("koinonia1", "Koinonia 1"),
                            ("koinonia2", "Koinonia 2"),
                            ("koinonia3", "Koinonia 3"),
                            ("koinonia4", "Koinonia 4"),
                            ("alfa", "Alfa"),
                            ("omega", "Omega"),
                            ("oasis", "Oasis"),
                        ),
                    ),
                    (
                        "Sector Centro",
                        (
                            ("agape1", "Ágape 1"),
                            ("agape2", "Ágape 2"),
                            ("agape3", "Ágape 3"),
                            ("agape4", "Ágape 4"),
                            ("huespedes1", "Huespedes 1"),
                            ("huespedes2", "Huespedes 2"),
                            ("huespedes3", "Huespedes 3"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("pastoral", "Pastoral"),
                        ),
                    ),
                    (
                        "Sector Campo",
                        (
                            ("moab", "Moab"),
                            ("esmirna", "Esmirna"),
                            ("efeso", "Éfeso"),
                            ("juda", "Judá"),
                            ("belen", "Belén"),
                            ("sinai", "Sinaí"),
                            ("gerisim", "Gerisim"),
                        ),
                    ),
                    (
                        "Sector Lago",
                        (
                            ("armenia", "Armenia"),
                            ("horeb", "Horeb"),
                            ("filadelfia", "Filadelfia"),
                            ("ebal", "Ebal"),
                            ("peniel", "Peniel"),
                            ("moria", "Moria"),
                        ),
                    ),
                ],
                max_length=16,
                verbose_name="Cabin",
            ),
        ),
    ]
