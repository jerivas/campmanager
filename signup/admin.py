from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core.urlresolvers import reverse

from signup.models import Camper, Payment, Counselor, Parent, Guest
from signup.filters import BalanceStatusFilter
from signup.actions import (move_permission_forward, move_permission_backwards,
                            generate_permission)


class PaymentInline(GenericTabularInline):
    model = Payment
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    """Base Admin for all Persons"""
    radio_fields = {"gender": admin.HORIZONTAL}
    list_per_page = 15
    _ld = ["names", "surnames"]
    list_display_links = ["names", "surnames"]
    _lf = ["gender"]
    _sf = ["^first_name", "^second_name", "^first_surname", "^second_surname"]


class PayerAdmin(admin.ModelAdmin):
    """Base Admin for all Payers"""
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


class MemberAdmin(admin.ModelAdmin):
    """Base admin for all Members (Campers and Counselors)"""
    _ld = ["structure", "generation", "small_group"]
    _rf = ["structure", "generation", "cabin", "bus"]
    _lf = ["structure", "generation", "small_group"]
    _sf = ["^structure", "^small_group__title", "bus", "cabin"]


class CamperAdmin(PersonAdmin, PayerAdmin, MemberAdmin):
    raw_id_fields = ("counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["counselor", "mother", "father"]}
    readonly_fields = PayerAdmin._rf + MemberAdmin._rf
    radio_fields = {"registrar_title": admin.HORIZONTAL,
                    "gender": admin.HORIZONTAL}

    fieldsets = [
        (_("Basic Info"), {"fields":
                           [("first_name", "second_name"),
                            ("first_surname", "second_surname"),
                            ("badge_name", "counselor"),
                            "gender",
                            ("no_pay", "fined"),
                            ("structure", "generation"),
                            ("cabin", "bus"),
                            ("balance_as_currency", "amount_due")]}),
        (_("Customs"), {"classes": ("grp-collapse grp-closed",),
                        "fields":
                        [("birth_date", "registrar_title"),
                        ("registrar", "registrar_position"),
                        ("birth_cert_num", "birth_cert_fol", "birth_cert_book"),
                        ("reg_state", "reg_province"),
                        ("state", "province"),
                        ("passport", "occupation"),
                        ("mother", "father"),
                        ("lawyer", "permission_status")]}),
    ]

    list_display = (PersonAdmin._ld + MemberAdmin._ld + PayerAdmin._ld
        + ["permission_status"])
    list_filter = MemberAdmin._lf + PayerAdmin._lf + ["permission_status"]
    list_editable = ["permission_status"]
    search_fields = (PersonAdmin._sf + MemberAdmin._sf
        + ["counselor__first_name", "counselor__second_name",
        "counselor__first_surname", "counselor__second_surname"])
    actions = [move_permission_forward, move_permission_backwards,
               generate_permission]


class CounselorAdmin(PersonAdmin, PayerAdmin, MemberAdmin):
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"]}
    readonly_fields = PayerAdmin._rf + MemberAdmin._rf

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("badge_name", "small_group"),
              "gender",
              ("no_pay", "fined"),
              ("structure", "generation"),
              ("cabin", "bus"),
              ("balance_as_currency", "amount_due"))

    list_display = PersonAdmin._ld + MemberAdmin._ld + PayerAdmin._ld
    list_filter = PersonAdmin._lf + MemberAdmin._lf + PayerAdmin._lf
    search_fields = PersonAdmin._sf + MemberAdmin._sf


class GuestAdmin(PersonAdmin, PayerAdmin):
    readonly_fields = PayerAdmin._rf

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("badge_name", "cabin"),
              "gender",
              ("no_pay", "fined"),
              ("balance_as_currency", "amount_due"))

    list_display = PersonAdmin._ld + ["cabin"] + PayerAdmin._ld
    list_editable = ["cabin"]
    list_filter = PersonAdmin._lf + ["cabin"] + PayerAdmin._lf
    search_fields = PersonAdmin._sf + ["cabin"]


class ParentAdmin(PersonAdmin):
    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("gov_id", "known_as"),
              "gender",
              "birth_date",
              ("state", "province"),
              "occupation")

    list_display = PersonAdmin._ld + ["known_as", "gender"]
    list_filter = PersonAdmin._lf
    search_fields = PersonAdmin._sf + ["known_as"]


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ["link_to_related"]

    fields = (("receipt_id", "payment_date"),
              ("amount", "notes"),
              "link_to_related")

    list_display = ["receipt_id", "amount", "payment_date", "link_to_related"]
    list_display_links = ["receipt_id", "amount"]
    date_hierarchy = "payment_date"
    search_fields = ["receipt_id", "notes", "camper__first_name",
    "counselor__first_name", "guest__first_name", "camper__first_surname",
    "counselor__first_surname", "guest__first_surname"]

    def link_to_related(self, model):
        m = model.content_object
        url_str = "admin:%s_%s_change" % (m._meta.app_label,
            m._meta.object_name.lower())
        m_url = reverse(url_str, args=[m.pk])
        return ("%s: <a href='%s'>%s</a><br>" %
                (m._meta.verbose_name.title(), m_url, m))
    link_to_related.short_description = _("Paid by")
    link_to_related.allow_tags = True

admin.site.register(Camper, CamperAdmin)
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Payment, PaymentAdmin)
