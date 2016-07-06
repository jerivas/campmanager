from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core.urlresolvers import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ExportMixin

from signup.models import Camper, Payment, Counselor, Parent, Guest
from signup.filters import BalanceStatusFilter
from signup.actions import (move_permission_forward, move_permission_backwards,
                            generate_permission)
from utils.admin import UnaccentSearchMixin

from .resources import CamperResource, PaymentResource, CounselorResource, GuestResource


class PaymentInline(GenericTabularInline):
    model = Payment
    extra = 1


class PersonMixin(UnaccentSearchMixin):
    """
    Base Admin for all Persons
    """
    radio_fields = {"gender": admin.HORIZONTAL}
    list_per_page = 50
    _ld = ["names", "surnames"]
    list_display_links = ["names", "surnames"]
    _sf = ["first_name__unaccent", "second_name__unaccent", "first_surname__unaccent",
           "second_surname__unaccent"]


class PayerMixin(object):
    """
    Base Admin for all Payers
    """
    inlines = [PaymentInline]
    _rf = ["balance_as_currency", "amount_due"]
    _ld = ["signed_up", "fined", "fully_paid", "balance_as_currency", "amount_due"]
    _lf = [BalanceStatusFilter]

    def save_related(self, request, form, formsets, change):
        """
        Save all InLine payments and then call the form"s save method.
        See Payer.save() in models.py to learn how the balance is updated.
        This prevents the balance from being updated with the sum of the old
        payments.
        """
        for payment in formsets:
            payment.save()
        form.save()

    def balance_as_currency(self, model):
        if model.no_pay:
            b = _("Doesn't pay")
        else:
            b = "$%s" % model.balance
        return b
    balance_as_currency.short_description = _("Balance")
    balance_as_currency.admin_order_field = "balance"

    def fully_paid(self, model):
        return model.fully_paid() or model.no_pay
    fully_paid.boolean = True
    fully_paid.short_description = _("Fully Paid")

    def amount_due(self, model):
        if model.no_pay:
            b = _("Doesn't pay")
        else:
            b = "$%s" % model.amount_due()
        return b
    amount_due.short_description = _("Amount Due")


class MemberMixin(object):
    """
    Common admin attributes for all Members.
    """
    _ld = ["structure", "generation", "small_group"]
    _rf = ["structure", "generation", "cabin", "bus"]
    _lf = ["structure", "generation", "small_group"]
    _sf = ["structure", "small_group__title__unaccent"]


@admin.register(Camper)
class CamperAdmin(ExportMixin, PersonMixin, PayerMixin, admin.ModelAdmin):
    resource_class = CamperResource
    change_list_template = "admin/signup/camper/change_list.html"
    raw_id_fields = ("counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["counselor", "mother", "father"]}
    readonly_fields = PayerMixin._rf + MemberMixin._rf
    radio_fields = {"registrar_title": admin.HORIZONTAL, "gender": admin.HORIZONTAL}

    fieldsets = [
        (_("Basic Info"), {
            "fields": [
                ("first_name", "second_name"),
                ("first_surname", "second_surname"),
                ("badge_name", "counselor"),
                ("gender", "has_medical_record"),
                ("no_pay", "fined"),
                ("structure", "generation"),
                ("cabin", "bus"),
                ("balance_as_currency", "amount_due"),
            ],
        }),
        (_("Customs"), {
            "fields": [
                ("birth_date", "registrar_title"),
                ("registrar", "registrar_position"),
                ("birth_cert_num", "birth_cert_fol", "birth_cert_book"),
                ("reg_state", "reg_province"),
                # Campers simply use their mother's state and province
                # ("state", "province"),
                ("passport", "occupation"),
                ("mother", "father"),
                ("lawyer", "permission_status")
            ],
            "classes": ["grp-collapse", "grp-closed"],
        }),
    ]

    list_select_related = ["small_group"]
    list_display = (PersonMixin._ld + ["has_medical_record"] + MemberMixin._ld +
                    PayerMixin._ld + ["permission_status"])
    list_filter = (["has_medical_record"] + MemberMixin._lf + PayerMixin._lf +
                   ["permission_status"])
    list_editable = ["permission_status"]
    search_fields = PersonMixin._sf + MemberMixin._sf
    actions = [move_permission_forward, move_permission_backwards, generate_permission]


@admin.register(Counselor)
class CounselorAdmin(ExportMixin, PersonMixin, PayerMixin, admin.ModelAdmin):
    resource_class = CounselorResource
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"]}
    readonly_fields = PayerMixin._rf + MemberMixin._rf

    fields = (
        ("first_name", "second_name"),
        ("first_surname", "second_surname"),
        ("badge_name", "small_group"),
        ("gender", "has_medical_record"),
        ("no_pay", "fined"),
        "has_gov_id",
        ("structure", "generation"),
        ("cabin", "bus"),
        ("balance_as_currency", "amount_due"),)

    list_select_related = ["small_group"]
    list_display = (PersonMixin._ld + ["has_medical_record", "has_gov_id"] +
                    MemberMixin._ld + PayerMixin._ld)
    list_filter = ["has_medical_record"] + MemberMixin._lf + PayerMixin._lf
    search_fields = PersonMixin._sf + MemberMixin._sf


@admin.register(Guest)
class GuestAdmin(ExportMixin, PersonMixin, PayerMixin, admin.ModelAdmin):
    resource_class = GuestResource
    readonly_fields = PayerMixin._rf

    fields = (
        ("first_name", "second_name"),
        ("first_surname", "second_surname"),
        ("badge_name", "cabin"),
        ("gender", "has_medical_record"),
        ("no_pay", "fined"),
        ("balance_as_currency", "amount_due"),)

    list_display = PersonMixin._ld + ["has_medical_record", "cabin"] + PayerMixin._ld
    list_editable = ["cabin"]
    list_filter = ["has_medical_record", "cabin"] + PayerMixin._lf
    search_fields = PersonMixin._sf + ["cabin"]


@admin.register(Parent)
class ParentAdmin(PersonMixin, admin.ModelAdmin):
    fields = (
        ("first_name", "second_name"),
        ("first_surname", "second_surname"),
        ("gov_id", "known_as"),
        "gender",
        "birth_date",
        ("state", "province"),
        "occupation",)

    list_display = PersonMixin._ld + ["known_as", "gender"]
    list_filter = ["gender"]
    search_fields = PersonMixin._sf + ["known_as__unaccent"]


@admin.register(Payment)
class PaymentAdmin(UnaccentSearchMixin, ExportMixin, admin.ModelAdmin):
    resource_class = PaymentResource
    readonly_fields = ["link_to_related"]

    fields = (
        ("receipt_id", "payment_date"),
        ("amount", "notes"),
        "link_to_related",)

    date_hierarchy = "payment_date"
    list_display_links = ["receipt_id", "amount"]
    list_display = ["receipt_id", "amount", "payment_date", "link_to_related"]
    search_fields = [
        "receipt_id", "notes__unaccent", "payer__first_name__unaccent",
        "payer__second_name__unaccent", "payer__first_surname__unaccent",
        "payer__second_surname__unaccent"]

    def has_add_permission(self, request):
        """
        Disable direct creation of new Payment instances.
        They should all be created via inlines only.
        """
        return False

    def link_to_related(self, model):
        """
        Show a link to the object attached to a particular Payment instance
        via a generic relation.
        """
        model = model.content_object
        meta = model._meta
        url_name = "admin:%s_%s_change" % (meta.app_label, meta.object_name.lower())
        url = reverse(url_name, args=[model.pk])
        return format_html("{}: <a href='{}'>{}</a><br>",
                           meta.verbose_name.title(), url, model)
    link_to_related.short_description = _("Paid by")
