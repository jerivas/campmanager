from django.db import models
from django.utils.translation import ugettext_lazy as _


class SmallGroup(models.Model):
    """A small group composed of several Campers and a Counselor"""
    from logistics.choices import GENERATIONS, STRUCTURES, CABINS, BUSES

    title = models.CharField(_("Title"), max_length=32, blank=False,
        unique=True)
    generation = models.PositiveIntegerField(_("Generation"), max_length=1,
        blank=False, choices=GENERATIONS, default=1)
    structure = models.CharField(_("Structure"), max_length=16, blank=True,
        choices=STRUCTURES)
    cabin = models.CharField(_("Cabin"), max_length=16, blank=True,
        choices=CABINS)
    bus = models.CharField(_("Bus"), max_length=16, blank=True,
        choices=BUSES)

    class Meta:
        ordering = ["generation"]
        verbose_name = _("Small Group")
        verbose_name_plural = _("Small Groups")
        permissions = (("view_reports", "View Reports"),
                       ("badge_report", "Badge Report"),)

    def __unicode__(self):
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
            self.counselor.save(update_fields=["structure", "generation",
                "cabin", "bus"])
        except Counselor.DoesNotExist:
            pass
        self.camper_set.update(structure=self.structure,
            generation=self.generation, cabin=self.cabin, bus=self.bus)

    def get_members(self):
        m = [self.counselor]
        m.extend(self.camper_set.all())
        return m

    @staticmethod
    def autocomplete_search_fields():
        return ("title__icontains", "structure__icontains")
