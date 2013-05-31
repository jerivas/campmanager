from django.db import models
from django.utils.translation import ugettext_lazy as _

from logistics.choices import GENERATION_MATCHING


class SmallGroup(models.Model):
    """A small group composed of several Campers and a Counselor"""
    from logistics.choices import GENERATIONS, STRUCTURES, CABINS, BUSES

    title = models.CharField(_("Title"), max_length=32, blank=False)
    generation = models.PositiveIntegerField(_("Generation"), max_length=1,
                                             blank=False, choices=GENERATIONS)
    structure = models.CharField(_("Structure"), max_length=16, blank=True,
                                 null=True, choices=STRUCTURES)
    cabin = models.CharField(_("Cabin"), max_length=16, blank=True, null=True,
                             choices=CABINS)
    bus = models.CharField(_("Bus"), max_length=16, blank=True, null=True,
                           choices=BUSES)

    class Meta:
        ordering = ["generation"]
        verbose_name = _("Small Group")
        verbose_name_plural = _("Small Groups")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        for structure in GENERATION_MATCHING:
            if self.generation in structure[1]:
                self.structure = structure[0]
        super(SmallGroup, self).save(*args, **kwargs)

    def camper_set(self):
        return self.counselor.camper_set.all()

    def member_set(self):
        return self.camper_set() | self.counselor

    @staticmethod
    def autocomplete_search_fields():
        return ("title__icontains", "structure__icontains")
