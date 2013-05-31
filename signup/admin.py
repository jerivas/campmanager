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
    _ld = ["names", "surnames"]
    _ldl = ["names", "surnames"]


class PayerAdmin(admin.ModelAdmin):
    """Base Admin for all Payers"""
    inlines = [PaymentInline, ]
    _rf = ["balance_as_currency", "amount_due"]
    _ld = ["fully_paid", "balance_as_currency", "amount_due"]

    def save_related(self, request, form, formsets, change):
        """
        Save all related payments and then call the form's save method.
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
    amount_due.admin_order_field = "-balance"


class CamperAdmin(PersonAdmin, PayerAdmin):
    raw_id_fields = ("counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["counselor", "mother", "father"]}
    readonly_fields = PayerAdmin._rf + ["cabin"]

    fieldsets = [
        (_("Basic Info"), {"fields":
                           [("first_name", "second_name"),
                           ("first_surname", "second_surname"),
                           "counselor",
                           "gender",
                           ("badge_name", "cabin"),
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

    list_display = (PersonAdmin._ld + ["small_group", "cabin", "generation",
                    "structure"] + PayerAdmin._ld
                    + ["docs_signed", "special_case"])
    list_display_links = PersonAdmin._ldl
    list_editable = ["docs_signed", "special_case"]


class CounselorAdmin(PersonAdmin, PayerAdmin):
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"]}
    readonly_fields = PayerAdmin._rf + ["cabin"]

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "small_group",
              "gender",
              ("badge_name", "cabin"),
              ("no_pay", "balance_as_currency", "amount_due"))

    list_display = PersonAdmin._ld + ["small_group", "cabin", "generation",
                                      "structure"] + PayerAdmin._ld
    list_display_links = PersonAdmin._ldl


class GuestAdmin(PersonAdmin, PayerAdmin):
    readonly_fields = PayerAdmin._rf

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("badge_name", "cabin"),
              "gender",
              ("no_pay", "balance_as_currency", "amount_due"))

    list_display = PersonAdmin._ld + ["cabin"] + PayerAdmin._ld
    list_display_links = PersonAdmin._ldl
    list_editable = ["cabin"]


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
