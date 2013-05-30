from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.timezone import now


class Person(models.Model):
    """Base class for all people"""
    GENDER_CHOICES = (
        ("m", _("Male")),
        ("f", _("Female")),
    )

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
        return "%s %s %s %s" % (self.first_name, self.second_name,
                                self.first_surname, self.second_surname)

    def names(self):
        return "%s %s" % (self.first_name, self.second_name)
    names.admin_order_field = "first_name"
    names.short_description = _("Names")

    def surnames(self):
        return "%s %s" % (self.first_surname, self.second_surname)
    surnames.admin_order_field = "first_surname"
    surnames.short_description = _("Surnames")


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

    def fully_paid(self):
        return self.balance == settings.CAMP_PRICE

    def amount_due(self):
        return settings.CAMP_PRICE - self.balance


class Payment(models.Model):
    """A payment done to pay the camps"s price"""
    receipt_id = models.CharField(_("Receipt ID"), max_length=16,
                 blank=False)
    payment_date = models.DateField(_("Date"), blank=True, null=True)
    amount = models.DecimalField(_("Amount"), max_digits=5,
             decimal_places=2, blank=False)
    notes = models.CharField(_("Notes"), max_length=256, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return "%s - $%s" % (self.receipt_id, self.amount)

    class Meta:
        ordering = ["-payment_date"]
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def save(self, *args, **kwargs):
        """Set default for ``payment_date`` as now"""
        if self.payment_date is None:
            self.payment_date = now()
        super(Payment, self).save(*args, **kwargs)


class Attendant(models.Model):
    """Basic model of anybody going to camp"""
    badge_name = models.CharField(_("Badge Name"), max_length=64,
                 blank=True, null=True)
    cabin = models.CharField(_("Cabin"), max_length=32, blank=True, null=True)

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

    class Meta(Person.Meta):
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")

    @staticmethod
    def autocomplete_search_fields():
        return ("first_name__icontains", "second_name__icontains",
                "first_surname__icontains", "second_surname__icontains")


class Camper(Person, ExtendedInfo, Payer, Minor, Attendant):
    """The main model of a child attending camp"""
    special_case = models.BooleanField(_("Special Case"),
                   blank=False, default=False)
    counselor = models.ForeignKey("Counselor", blank=False)

    class Meta(Person.Meta):
        verbose_name = _("Camper")
        verbose_name_plural = _("Campers")

    def small_group(self):
        return self.assigned_counselor.small_group
    small_group.short_description = _("Small Group")

    def generation(self):
        return self.small_group.generation
    generation.short_description = _("Generation")

    def structure(self):
        return self.small_group.structure
    structure.short_description = _("Structure")


class Counselor(Person, Payer, Attendant):
    """A counselor for campers"""
    small_group = models.OneToOneField("logistics.SmallGroup", blank=False)

    class Meta(Person.Meta):
        verbose_name = _("Counselor")
        verbose_name_plural = _("Counselors")

    def generation(self):
        return self.small_group.generation
    generation.short_description = _("Generation")

    def structure(self):
        return self.generation().structure
    structure.short_description = _("Structure")

    def related_label(self):
        return "%s %s (%s)" % (self.names(), self.first_surname,
                               self.small_group)

    @staticmethod
    def autocomplete_search_fields():
        return ("first_name__icontains", "first_surname__icontains",
                "badge_name__icontains", "small_group__title__icontains")


class Guest(Person, Payer, Attendant):
    """An attendant that doesn't belong to a small group"""

    class Meta(Person.Meta):
        verbose_name = _("Guest")
        verbose_name_plural = _("Guests")