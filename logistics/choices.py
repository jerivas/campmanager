# -*- coding: utf-8 -*-

GENERATIONS = (
    (1, "Josías 1"),
    (2, "Josías 2"),
    (3, "Freshmen"),
    (4, "Sophomores"),
    (5, "Juniors"),
    (6, "Seniors"),
    (7, "La Red"),
    (8, "G180"),
)

STRUCTURES = (
    ("josias", "Josías"),
    ("preju", "Preju"),
    ("lared", "La Red"),
    ("g180", "G180"),
)

CABINS = (
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
)

BUSES = (
    ("1", "Bus 1"),
    ("2", "Bus 2"),
    ("3", "Bus 3"),
    ("4", "Bus 4"),
    ("5", "Bus 5"),
    ("6", "Bus 6"),
    ("7", "Bus 7"),
)

GENERATION_MATCHING = (
    ("josias", (1, 2)),
    ("preju", (3, 4, 5, 6)),
    ("lared", (7,)),
    ("g180", (8,)),
)
