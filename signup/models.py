import locale

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse


class Person(models.Model):
    """Base class for all people"""
    from signup.choices import GENDER_CHOICES

    first_name = models.CharField(_("First Name"),
                 max_length=64, blank=False)
    second_name = models.CharField(_("Second Name"),
                  max_length=64, blank=False)
    first_surname = models.CharField(_("First Surname"),
                    max_length=64, blank=False)
    second_surname = models.CharField(_("Second Surname"),
                     max_length=64, blank=False)    
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES,
             max_length=1, blank=False)

    class Meta:
        ordering = ["first_surname"]
        abstract = True

    def __unicode__(self):
        return "%s %s %s" % (self.first_name, self.second_name,
                             self.first_surname)


class ExtendedInfo(models.Model):
    """Extra info about some people"""
    from signup.choices import STATE_CHOICES

    birth_date = models.DateTimeField(_("Birth Date"), blank=True, null=True)
    state = models.CharField(_("State"), max_length=3,
            choices=STATE_CHOICES, blank=True, null=True)
    province = models.CharField(_("Province"), max_length=32,
               blank=True, null=True)
    occupation = models.CharField(_("Occupation"), max_length=32,
                 blank=True, null=True)

    class Meta:
        abstract = True


class Payer(models.Model):
    """Class for anyone who has to pay"""
    balance = models.DecimalField(_("Balance"), max_digits=5,
              decimal_places=2, blank=False, default=0)
    no_pay = models.BooleanField(_("Doesn't pay"), blank=False,
             default=False)
    payment_set = generic.GenericRelation("Payment")

    class Meta:
        abstract = True

    def balance_as_currency(self):
        return locale.currency(self.balance)

    def fully_paid(self):
        return self.balance == settings.CAMP_PRICE

    def amount_due(self):
        return settings.CAMP_PRICE - self.balance


class Payment(models.Model):
    """A payment done to pay the camps's price"""
    receipt_id = models.CharField(_("Receipt ID"), max_length=16,
                 blank=False)
    payment_date = models.DateField(_("Date"), blank=False)
    amount = models.DecimalField(_("Amount"), max_digits=5,
             decimal_places=2, blank=False)
    notes = models.CharField(_("Notes"), max_length=256, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return "$%s - $%s" % (self.receipt_id, self.amount)

    class Meta:
        ordering = ["-payment_date"]


class Attendant(models.Model):
    """Basic model of anybody going to camp"""
    badge_name = models.CharField(_("Badge Name"), max_length=64,
                 blank=True, null=True)

    class Meta:
        abstract = True


class Minor(models.Model):
    """Basic model applying to minors for permission handling"""
    passport = models.CharField(_("Passport Number"), max_length=16,
               blank=True, null=True)
    birth_cert_num = models.PositiveIntegerField(_("Birth Certificate Number"),
                     blank=True, null=True)
    birth_cert_fol = models.PositiveIntegerField(_("Birth Certificate Folio"),
                     blank=True, null=True)
    birth_cert_book = models.PositiveIntegerField(_("Birth Certificate Book"),
                      blank=True, null=True)
    registrar = models.CharField(_("Birth Certificate Registrar"),
                max_length=256, blank=True, null=True)
    docs_signed = models.BooleanField(_("Signed documents"), blank=False,
                  default=False)
    mother = models.ForeignKey("Parent", related_name="mothered",
             blank=True, null=True)
    father = models.ForeignKey("Parent", related_name="fathered",
             blank=True, null=True)

    class Meta:
        abstract = True


class Parent(Person, ExtendedInfo):
    """A parent or legal guardian of a minor"""
    gov_id = models.CharField(_("ID Number"), max_length=16, blank=False)


class Camper(Person, ExtendedInfo, Payer, Minor, Attendant):
    """The main model of a child attending camp"""
    special_case = models.BooleanField(_("Special Case"),
                   blank=False, default=False)
    assigned_counselor = models.ForeignKey("Counselor", blank=True, null=True)

    def small_group(self):
        return self.assigned_counselor.small_group

    def generation(self):
        return self.small_group.generation

    def structure(self):
        return self.small_group.structure

    def cabin(self):
        return self.small_group.cabin


class Counselor(Person, Payer, Attendant):
    """A counselor for campers"""
    small_group = models.OneToOneField("logistics.SmallGroup", blank=False)

    def generation(self):
        return self.small_group.generation

    def structure(self):
        return self.small_group.structure

    def cabin(self):
        return self.small_group.cabin
