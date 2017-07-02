from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel

from signup.models import Person, ExtendedInfo
from signup.validators import gov_id_validator
from siterelated.models import SiteRelated
from siterelated.utils import current_site_id, override_current_site_id


@python_2_unicode_compatible
class Camp(SiteRelated, SingletonModel):
    """
    Singleton model to store general camp information.
    """
    title = models.CharField(_("Title"), max_length=75)
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    signup_fee = models.DecimalField(
        _("Signup fee"), max_digits=5, decimal_places=2)
    fine = models.DecimalField(_("Fine"), max_digits=5, decimal_places=2)
    destination = models.CharField(
        _("Destination"), max_length=75, help_text=_("The Republic of..."))
    duration = models.CharField(
        _("Duration"), max_length=100, help_text=_("Text describing the "
                                                   "camp's duration"))
    permission_timestamp = models.DateTimeField(
        _("Permission timestamp"),
        help_text=_("The date and time when the permissions are signed"))
    permission_location = models.CharField(
        _("Permission location"), max_length=75,
        help_text=_("The location where the permission are signed"))

    class Meta:
        verbose_name = verbose_name_plural = _("Camp")

    def __str__(self):
        return self.title

    @classmethod
    def get_cache_key(cls):
        """
        Modify Solo's cache key to be unique per-site.
        """
        prefix = super(Camp, cls).get_cache_key()
        return "%s:%s" % (current_site_id(), prefix)


@receiver(models.signals.post_save, sender=Site)
def create_camp(sender, instance, created, *args, **kwargs):
    """
    Create a Camp whenever a new site is created.
    """
    if not created:
        return
    with override_current_site_id(instance.id):
        Camp.objects.create(
            title="Untitled",
            price=0,
            signup_fee=0,
            fine=0,
            destination="Unknown",
            duration="Unknown",
            permission_timestamp=now(),
            permission_location="Unknown"
        )


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
