from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

"""
Validates a Salvadorean Government ID. 8 numbers, a dash and
another number (check digit). The check digit is not actually
calculated.
"""
gov_id_validator = RegexValidator(regex=r"^\d{8}-\d$",
    message=_("Invalid Government ID"))
