from django.utils.translation import ugettext_lazy as _

MALE = "m"
FEMALE = "f"
GENDER_CHOICES = (
    (MALE, _("Male")),
    (FEMALE, _("Female")),
)

STATE_CHOICES = (
    ("ahu", _("Ahuachapan")),
    ("saa", _("Santa Ana")),
    ("son", _("Sonsonate")),
    ("usu", _("Usulutan")),
    ("sam", _("San Miguel")),
    ("mor", _("Morazan")),
    ("lau", _("La Union")),
    ("lal", _("La Libertad")),
    ("cha", _("Chalatenango")),
    ("cus", _("Cuscatlan")),
    ("sas", _("San Salvador")),
    ("lap", _("La Paz")),
    ("cab", _("Cabanas")),
    ("sav", _("San Vicente")),
)
