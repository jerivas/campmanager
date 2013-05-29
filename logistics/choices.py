from django.utils.translation import ugettext_lazy as _

PREJU = "Preju"
JOSIAS = "JOSIAS"
STRUCTURE_CHOICES = (
    (PREJU, _("Preju")),
    (JOSIAS, _("Josias")),
)

JOSIAS1 = 1
JOSIAS2 = 2
FRESHMEN = 3
SOPHOMORES = 4
JUNIORS = 5
SENIORS = 6
GENERATION_CHOICES = (
    (JOSIAS1, _("Josias 1")),
    (JOSIAS2, _("Josias 2")),
    (FRESHMEN, _("Freshmen")),
    (SOPHOMORES, _("Sophomores")),
    (JUNIORS, _("Juniors")),
    (SENIORS, _("Seniors")),
)
