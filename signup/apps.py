from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SignupConfig(AppConfig):
    name = "signup"
    verbose_name = _("Signup")
