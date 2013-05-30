from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from signup.models import Camper, Payment, Counselor, Parent, Guest


class PaymentInline(generic.GenericTabularInline):
    model = Payment
    extra = 1


class HideFromAdminList(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class PersonAdmin(admin.ModelAdmin):
    """Base Admin for all Persons"""
    radio_fields = {"gender": admin.HORIZONTAL}
    list_display = ("names", "surnames")
    list_display_links = ("names", "surnames")


class PayerAdmin(admin.ModelAdmin):
    """Base Admin for all Payers"""
    inlines = (PaymentInline,)

    def balance_as_currency(self, model):
        if model.no_pay:
            b = _("Doesn't pay")
        else:
            b = "$%s" % model.balance
        return b
    balance_as_currency.short_description = _("Balance as Currency")

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


class CamperAdmin(PersonAdmin, PayerAdmin):
    raw_id_fields = ("counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["counselor", "mother", "father"]}
    readonly_fields = ("balance_as_currency", "amount_due", "cabin")

    fieldsets = [
        (_("Basic Info"), {"fields":
                           [("first_name", "second_name"),
                           ("first_surname", "second_surname"),
                           "badge_name",
                           "gender",
                           ("counselor", "cabin"),
                           ("no_pay", "balance_as_currency", "amount_due")]}),
        (_("Customs"), {"classes": ("grp-collapse grp-closed",),
                        "fields":
                         [("special_case", "docs_signed"),
                         "birth_date",
                         ("state", "province"),
                         "occupation",
                         "passport",
                         ("birth_cert_num", "birth_cert_fol", "birth_cert_book"),
                         "registrar",
                         "mother",
                         "father"]}),
    ]

    list_display = ("names", "surnames", "small_group", "cabin", "generation",
                    "structure", "fully_paid", "amount_due", "docs_signed",
                    "special_case")

    list_editable = ("docs_signed", "special_case")


class CounselorAdmin(PersonAdmin, PayerAdmin):
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"]}
    readonly_fields = ("balance_as_currency", "amount_due", "cabin")

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "badge_name",
              "gender",
              "small_group",
              ("no_pay", "balance_as_currency", "amount_due"))

    list_display = ("names", "surnames", "small_group", "cabin", "generation",
                    "structure", "fully_paid", "amount_due")


class GuestAdmin(PersonAdmin, PayerAdmin):
    readonly_fields = ("balance_as_currency", "amount_due", "cabin")

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("badge_name", "cabin"),
              "gender",
              ("no_pay", "balance_as_currency", "amount_due"))

    list_display = ("names", "surnames", "cabin", "fully_paid", "amount_due")


class ParentAdmin(PersonAdmin, HideFromAdminList):
    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "gov_id",
              "gender",
              "birth_date",
              ("state", "province"),
              "occupation")

admin.site.register(Camper, CamperAdmin)
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Payment, HideFromAdminList)
