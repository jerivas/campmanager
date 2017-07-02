from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from siterelated.models import SiteRelated


@python_2_unicode_compatible
class SmallGroup(SiteRelated):
    """
    A small group composed of several Campers and a Counselor
    """
    from logistics.choices import GENERATIONS, STRUCTURES, CABINS, BUSES

    title = models.CharField(_("Title"), max_length=32, unique=True)
    generation = models.PositiveIntegerField(
        _("Generation"), choices=GENERATIONS, default=1)
    structure = models.CharField(
        _("Structure"), max_length=16, blank=True, choices=STRUCTURES)
    cabin = models.CharField(
        _("Cabin"), max_length=16, blank=True, choices=CABINS)
    bus = models.CharField(
        _("Bus"), max_length=16, blank=True, choices=BUSES)

    class Meta:
        ordering = ["generation"]
        verbose_name = _("Small Group")
        verbose_name_plural = _("Small Groups")
        permissions = (("view_reports", "View Reports"),
                       ("attendant_report", "Attendant Report"),)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        This method matches the structure to the selected generation via
        the GENERATION_MATCHING tuple. It then saves the object and proceeds
        to update all related objects (Campers and Counselor). An Exception is
        catched if the Counselor hasn't been assigned yet (because the
        Small Group might be new, for example).
        """
        from logistics.choices import GENERATION_MATCHING
        from signup.models import Counselor

        for structure in GENERATION_MATCHING:
            if self.generation in structure[1]:
                self.structure = structure[0]
        super(SmallGroup, self).save(*args, **kwargs)
        try:
            self.counselor.save(
                update_fields=["structure", "generation", "cabin", "bus"])
        except Counselor.DoesNotExist:
            pass
        self.camper_set.update(
            structure=self.structure,
            generation=self.generation,
            cabin=self.cabin,
            bus=self.bus
        )

    def get_members(self, signed_up=None):
        """
        Allows filtering Small Group members by signup status.
        """
        members = []
        if signed_up is None:
            members.append(self.counselor)
            members.extend(self.camper_set.all())
        else:
            if self.counselor.signed_up == signed_up:
                members.append(self.counselor)
            members.extend(self.camper_set.filter(signed_up=signed_up))
        return members

    def get_attendants(self):
        """
        Simple wrapper to call get_members() from templates with signed_up=True
        """
        return self.get_members(signed_up=True)

    @staticmethod
    def autocomplete_search_fields():
        return ("title__icontains", "structure__icontains")
