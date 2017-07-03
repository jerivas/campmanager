from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from solo.templatetags.solo_tags import get_solo

from logistics.choices import STRUCTURES, GENERATIONS, CABINS, BUSES
from signup.choices import STATES
from signup.validators import gov_id_validator
from siterelated.models import SiteRelated


####################
# Abstract classes #
####################

@python_2_unicode_compatible
class Person(models.Model):
    """
    Basic information about a person.
    """
    GENDER_CHOICES = (
        ("m", _("Male")),
        ("f", _("Female")),
    )

    first_name = models.CharField(_("First Name"), max_length=64)
    second_name = models.CharField(_("Second Name"), max_length=64, blank=True)
    first_surname = models.CharField(_("First Surname"), max_length=64)
    second_surname = models.CharField(_("Second Surname"), max_length=64, blank=True)
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES, max_length=1)

    class Meta:
        ordering = ["first_surname"]
        unique_together = (
            "first_name", "second_name", "first_surname", "second_surname")
        abstract = True

    def __str__(self):
        return " ".join([self.names(), self.surnames()])

    def names(self):
        return " ".join([self.first_name, self.second_name]).strip()
    names.admin_order_field = "first_name"
    names.short_description = _("Names")

    def surnames(self):
        return " ".join([self.first_surname, self.second_surname]).strip()
    surnames.admin_order_field = "first_surname"
    surnames.short_description = _("Surnames")


class ExtendedInfo(models.Model):
    """
    Extra info about a person.
    """
    birth_date = models.DateTimeField(
        _("Birth Date"), blank=True, null=True,
        help_text=_("The format is YYYY-MM-DD and 24 hour time."))
    state = models.CharField(_("State"), max_length=3, blank=True, choices=STATES)
    province = models.CharField(_("Province"), max_length=32, blank=True)
    occupation = models.CharField(_("Occupation"), max_length=99, blank=True)

    class Meta:
        abstract = True

    def age(self):
        """
        Get the age of this person, accounting for leap years.
        """
        if self.birth_date is not None:
            try:
                birthday = self.birth_date.replace(year=now().year)
            except ValueError:
                # raised when birth date is February 29 and the current year is
                # not a leap year
                birthday = self.birth_date.replace(year=now().year,
                                                   day=self.birth_date.day - 1)
            return now().year - self.birth_date.year - (birthday > now())


class Minor(models.Model):
    """
    Basic model applying to minors for permission handling.
    """
    TITLES = (
        ("m", _("Mr.")),
        ("f", _("Mrs.")),
    )

    INCOMPLETE = 0
    TO_PRINT = 1
    PRINTED = 2
    SIGNED = 3
    PROOFREAD = 4
    SPECIAL = 5
    PENDING_ID = 6
    SUBMITTED_ID = 7

    PERMISSION_STATUS = (
        (_("Minors"), (
            (INCOMPLETE, _("Pending Documentation")),
            (TO_PRINT, _("Ready to Print")),
            (PRINTED, _("Printed")),
            (SIGNED, _("Signed")),
            (PROOFREAD, _("Proofread")),
            (SPECIAL, _("Special Case")),
        )),
        (_("Adults"), (
            (PENDING_ID, _("Pending ID")),
            (SUBMITTED_ID, _("Submitted ID")),
        )),
    )

    lawyer = models.ForeignKey(
        "general.Lawyer", verbose_name=_("Assigned Lawyer"), blank=True, null=True)
    passport = models.CharField(_("Passport Number"), max_length=16, blank=True)
    birth_cert_num = models.PositiveIntegerField(
        _("Birth Certificate Number"), blank=True, null=True)
    birth_cert_fol = models.PositiveIntegerField(
        _("Birth Certificate Folio"), blank=True, null=True)
    birth_cert_book = models.PositiveIntegerField(
        _("Birth Certificate Book"), blank=True, null=True)
    registrar = models.CharField(
        _("Birth Certificate Registrar"), max_length=256, blank=True)
    registrar_title = models.CharField(
        _("Birth Certificate Registrar Title"), max_length=16, blank=True,
        choices=TITLES)
    registrar_position = models.CharField(
        _("Birth Certificate Registrar Position"), max_length=100, blank=True,
        help_text=_("Position at the municipality"))
    reg_state = models.CharField(
        _("Registration State"), max_length=3, blank=True, choices=STATES)
    reg_province = models.CharField(
        _("Registration Province"), max_length=32, blank=True)
    mother = models.ForeignKey(
        "Parent", related_name="mothered", blank=True, null=True,
        verbose_name=_("Mother"))
    father = models.ForeignKey(
        "Parent", related_name="fathered", blank=True, null=True,
        verbose_name=_("Father"))
    permission_status = models.IntegerField(
        _("Permission Status"), choices=PERMISSION_STATUS, default=INCOMPLETE)

    class Meta:
        abstract = True


class Payer(models.Model):
    """
    Financial information related to a camp attendant.
    """
    signed_up = models.BooleanField(_("Signed up"), default=False)
    balance = models.DecimalField(
        _("Balance"), max_digits=5, decimal_places=2, default=0)
    no_pay = models.BooleanField(
        _("Doesn't pay"), default=False,
        help_text=_("Mark if this person is exempt of the camp's price"))
    fined = models.BooleanField(
        _("Fined"), default=False, help_text=_("This person must pay a fine"))
    payment_set = GenericRelation("Payment", related_query_name="payer")

    class Meta:
        abstract = True

    def get_price(self):
        """
        Calculates the price this person has to pay to  attend camp. The price
        varies depending on the fine.
        """
        camp = get_solo("general.Camp")  # Get the camp information

        price = camp.price
        if self.fined:
            price += camp.fine
        return price

    def fully_paid(self):
        return self.balance == self.get_price()

    def amount_due(self):
        return self.get_price() - self.balance
    amount_due.short_description = _("Amount Due")

    def save(self, *args, **kwargs):
        """
        Update the balance and signed_up status.
        """
        camp = get_solo("general.Camp")  # Get the camp information

        if self.payment_set.count() > 0:
            self.balance = sum(p.amount for p in self.payment_set.all())
        else:
            self.balance = 0
        if self.no_pay or self.balance >= camp.signup_fee:
            self.signed_up = True
        else:
            self.signed_up = False
        super(Payer, self).save(*args, **kwargs)


class Attendant(models.Model):
    """
    Logistics information related to a camp attendant.
    """
    badge_name = models.CharField(
        _("Badge Name"), max_length=64, blank=True,
        help_text=_("The name that appears in the badge."))
    cabin = models.CharField(_("Cabin"), max_length=16, blank=True, choices=CABINS)
    has_medical_record = models.BooleanField(
        _("Medical record"), blank=True, default=False,
        help_text=_("This person has submitted their medical record"))

    class Meta:
        abstract = True


class Member(models.Model):
    """
    A member of a Small Group and Structure (Campers and Counselors)
    """
    generation = models.PositiveIntegerField(_("Generation"), choices=GENERATIONS)
    structure = models.CharField(
        _("Structure"), max_length=16, blank=True, choices=STRUCTURES)
    bus = models.CharField(_("Bus"), max_length=16, blank=True, choices=BUSES)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        This method only works if the subclasses of Member have a
        small_group field.
        """
        self.generation = self.small_group.generation
        self.structure = self.small_group.structure
        self.cabin = self.small_group.cabin
        self.bus = self.small_group.bus
        super(Member, self).save(*args, **kwargs)


###################
# Concrete models #
###################

@python_2_unicode_compatible
class Payment(SiteRelated):
    """
    A generic payment done by anyone attending camp.
    """
    receipt_id = models.PositiveIntegerField(_("Receipt ID"), unique=True)
    payment_date = models.DateField(_("Date"), blank=True, null=True)
    amount = models.DecimalField(_("Amount"), max_digits=5, decimal_places=2)
    notes = models.CharField(_("Notes"), max_length=256, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return "%s - $%s" % (self.receipt_id, self.amount)

    class Meta:
        ordering = ["-receipt_id"]
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def save(self, *args, **kwargs):
        """
        Set default for ``payment_date`` as now.
        """
        if self.payment_date is None:
            self.payment_date = now()
        super(Payment, self).save(*args, **kwargs)


class Parent(SiteRelated, Person, ExtendedInfo):
    """
    A parent or legal guardian of a minor.
    """
    gov_id = models.CharField(
        _("ID Number"), max_length=10, validators=[gov_id_validator])
    known_as = models.CharField(_("Known as"), max_length=255, blank=True)

    class Meta(Person.Meta):
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")

    @staticmethod
    def autocomplete_search_fields():
        """
        Lookups used by Grappelli when looking for parents as FK.
        """
        return ("first_name__icontains", "second_name__icontains",
                "first_surname__icontains", "second_surname__icontains")


class Camper(SiteRelated, Person, ExtendedInfo, Payer, Minor, Attendant, Member):
    """
    The main model of a person attending camp.
    """
    counselor = models.ForeignKey(
        "Counselor", verbose_name=_("Counselor or Small Group"))
    small_group = models.ForeignKey(
        "logistics.SmallGroup", blank=True, null=True, verbose_name=_("Small Group"))

    class Meta(Person.Meta):
        verbose_name = _("Camper")
        verbose_name_plural = _("Campers")
        permissions = (("generate_permission", "Generate Permission"),)

    def save(self, *args, **kwargs):
        """
        Get the small_group from the Counselor.
        """
        self.small_group = self.counselor.small_group
        super(Camper, self).save(*args, **kwargs)


class Counselor(SiteRelated, Person, Payer, Attendant, Member):
    """
    A counselor for campers.
    """
    has_gov_id = models.BooleanField(
        _("ID on file"), blank=True, default=False,
        help_text=_("This person has filed a copy of their ID"))
    small_group = models.OneToOneField(
        "logistics.SmallGroup", verbose_name=_("Small Group"))

    class Meta(Person.Meta):
        verbose_name = _("Counselor")
        verbose_name_plural = _("Counselors")

    def related_label(self):
        return "%s %s (%s)" % (self.names(), self.first_surname,
                               self.small_group)

    @staticmethod
    def autocomplete_search_fields():
        """
        Lookups used by Grappelli when looking for Counselors as FK.
        """
        return ("first_name__icontains", "first_surname__icontains",
                "badge_name__icontains", "small_group__title__icontains")


class Guest(SiteRelated, Person, Payer, Attendant):
    """
    An attendant that doesn't belong to a small group.
    """

    class Meta(Person.Meta):
        verbose_name = _("Guest")
        verbose_name_plural = _("Guests")
