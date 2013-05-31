from django.utils.translation import ugettext_lazy as _

GENERATIONS = (
    (1, _("Josias 1")),
    (2, _("Josias 2")),
    (3, _("Freshmen")),
    (4, _("Sophomores")),
    (5, _("Juniors")),
    (6, _("Freshmen"))
)

STRUCTURES = (
    ("preju", _("Preju")),
    ("josias", _("Josias")),
)

CABINS = (
    ("huespedes", _("Huespedes")),
    ("betel", _("Betel")),
    ("shekinah", _("Shekinah")),
)

BUSES = (
    ("1", _("Bus 1")),
    ("2", _("Bus 2")),
    ("3", _("Bus 3")),
    ("4", _("Bus 4")),
)

GENERATION_MATCHING = (
    ("josias", (1, 2)),
    ("preju", (3, 4, 5, 6))
)
