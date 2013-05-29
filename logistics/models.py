from django.db import models
from django.utils.translation import ugettext_lazy as _


class SmallGroup(models.Model):
    """A small group with a bunch of helpful methods"""
    from logistics.choices import GENERATION_CHOICES

    title = models.CharField(_("Title"), max_length=32, blank=False)
    cabin = models.ForeignKey("Cabin", blank=True, null=True)
    generation = models.PositiveIntegerField(_("Generation"),
                 choices=GENERATION_CHOICES, blank=False)
    bus = models.ForeignKey("Bus", blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title

    def structure(self):
        return self.generation.structure

    def members(self):
        return self.counselor.camper_set.all()

    def member_count(self):
        return self.counselor.camper_set.count()


class Cabin(models.Model):
    """A cabin where campers live during camp"""
    title = models.CharField(_("Title"), max_length=32, blank=False)

    def __unicode__(self):
        return self.title


class Bus(models.Model):
    """A bus on which small groups travel"""
    title = models.CharField(_("Title"), max_length=32, blank=False)
    responsible = models.OneToOneField("signup.Counselor",
                  blank=True, null=True)

    def __unicode__(self):
        return self.title
