from django.db import models
from django.utils.translation import ugettext_lazy as _


class SmallGroup(models.Model):
    """A small group composed of several Campers and a Counselor"""
    title = models.CharField(_("Title"), max_length=32, blank=False)
    cabin = models.ForeignKey("Cabin", blank=True, null=True)
    generation = models.ForeignKey("Generation", blank=False)
    bus = models.ForeignKey("Bus", blank=True, null=True)

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

    age = models.PositiveIntegerField(_("Age"), blank=False)
    title = models.CharField(_("Title"), max_length=32, blank=False)
    structure = models.CharField(_("Structure"), max_length=32,
                choices=STRUCTURE_CHOICES, blank=False)

    class Meta:
        ordering = ["age"]
        verbose_name = _("Generation")
        verbose_name_plural = _("Generations")

    def __unicode__(self):
        return self.title


class Cabin(models.Model):
    """A cabin where campers live during camp"""
    title = models.CharField(_("Title"), max_length=32, blank=False)

    class Meta:
        verbose_name = _("Cabin")
        verbose_name_plural = _("Cabins")

    def __unicode__(self):
        return self.title


class Bus(models.Model):
    """A bus on which small groups travel"""
    title = models.CharField(_("Title"), max_length=32, blank=False)
    responsible = models.OneToOneField("signup.Counselor",
                  blank=True, null=True)

    class Meta:
        verbose_name = _("Bus")
        verbose_name_plural = _("Buses")

    def __unicode__(self):
        return self.title
