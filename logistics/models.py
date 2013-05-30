from django.db import models
from django.utils.translation import ugettext_lazy as _


class SmallGroup(models.Model):
    """A small group composed of several Campers and a Counselor"""
    from logistics.choices import CABIN_CHOICES, BUS_CHOICES

    title = models.CharField(_("Title"), max_length=32, blank=False)
    generation = models.ForeignKey("Generation", blank=False,
                                   related_name="small_group_set")
    cabin = models.CharField(_("Cabin"), max_length=32, choices=CABIN_CHOICES,
                             blank=True, null=True)
    bus = models.CharField(_("Bus"), max_length=32, choices=BUS_CHOICES,
                           blank=True, null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = _("Small Group")
        verbose_name_plural = _("Small Groups")

    def __unicode__(self):
        return self.title

    def structure(self):
        return self.generation.structure

    def camper_set(self):
        return self.counselor.camper_set.all()

    def member_set(self):
        return self.camper_set() | self.counselor

    @staticmethod
    def autocomplete_search_fields():
        return ("title__icontains", "generation__title__icontains",
                "generation__structure__icontains")


class Generation(models.Model):
    """A generation for grouping small groups"""
    from logistics.choices import STRUCTURE_CHOICES

    age = models.PositiveIntegerField(_("Age"), blank=False, unique=True)
    title = models.CharField(_("Title"), max_length=32, blank=False)
    structure = models.CharField(_("Structure"), max_length=32,
                choices=STRUCTURE_CHOICES, blank=False)

    class Meta:
        ordering = ["age"]
        verbose_name = _("Generation")
        verbose_name_plural = _("Generations")

    def __unicode__(self):
        return self.title
