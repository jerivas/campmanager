from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel

from signup.models import Person, ExtendedInfo
from signup.validators import gov_id_validator


@python_2_unicode_compatible
class Camp(SingletonModel):
    """
    Singleton model to store general camp information.
    """
    title = models.CharField(_("Title"), max_length=75)
    destination = models.CharField(
        _("Destination"), max_length=75, help_text=_("The Republic of..."))
    start = models.DateField(_("Start date"))
    end = models.DateField(_("End date"))
    permission_timestamp = models.DateTimeField(
        _("Permission timestamp"),
        help_text=_("The date and time when the permissions are signed"))
    permission_location = models.CharField(
        _("Permission location"), max_length=75,
        help_text=_("The location where the permission are signed"))

    class Meta:
        verbose_name = _("Camp")

    def __str__(self):
        return self.title


class Chaperone(Person, ExtendedInfo):
    """
    A chaperone listed as responsible for the camp in the permissions.
    """
    camp = models.OneToOneField(Camp, verbose_name=_("Camp"))
    gov_id = models.CharField(
        _("ID Number"), max_length=10, validators=[gov_id_validator])

    class Meta:
        verbose_name = _("Chaperone")


class Lawyer(Person):
    """
    A Lawyer capable of signing permissions for the camp.
    """
    camp = models.ForeignKey(Camp, verbose_name=_("Camp"))

    class Meta:
        verbose_name = _("Lawyer")
        verbose_name_plural = _("Lawyers")
