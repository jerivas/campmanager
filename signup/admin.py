from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.admin import SimpleListFilter
from django.conf import settings

from signup.models import Camper, Payment, Counselor, Parent, Guest


class FullyPaidFilter(SimpleListFilter):
    """Allows filtering Payers who had fully paid the camp price"""
    title = _("Balance Status")
    parameter_name = "balance"

    def lookups(self, request, model_admin):
        return (
            ("under", _("Under price")),
            ("full", _("Equals price")),
            ("over", _("Over price")),
        )

    def queryset(self, request, queryset):
        price = settings.CAMP_PRICE
        if self.value() == "under":
            return queryset.filter(balance__lt=price)
        if self.value() == "full":
            return queryset.filter(balance__exact=price)
        if self.value() == "over":
            return queryset.filter(balance__gt=price)


class PaymentInline(generic.GenericTabularInline):
    model = Payment
    extra = 1


class HideFromAdminList(admin.ModelAdmin):
    def get_model_perms(self, request):
        """Return empty perms dict thus hiding the model from admin index."""
        return {}


class PersonAdmin(admin.ModelAdmin):
    """Base Admin for all Persons"""
    radio_fields = {"gender": admin.HORIZONTAL}
    _ld = ["names", "surnames"]
    list_display_links = ["names", "surnames"]
    _lf = ["gender"]
    _sf = ["first_name", "second_name", "first_surname", "second_surname"]


class PayerAdmin(admin.ModelAdmin):
    """Base Admin for all Payers"""
    inlines = [PaymentInline]
    _rf = ["balance_as_currency", "amount_due"]
    _ld = ["fully_paid", "balance_as_currency", "amount_due"]
    _lf = [FullyPaidFilter]

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
    _ld = ["dspl_structure", "dspl_generation", "small_group"]
    _rf = ["structure", "generation", "cabin", "bus"]
    _lf = ["structure", "generation", "small_group"]
    _sf = ["structure", "small_group__title", "cabin", "bus"]

    def dspl_structure(self, model):
        return model.get_structure_display()
    dspl_structure.short_description = _("Structure")
    dspl_structure.admin_order_field = "structure"

    def dspl_generation(self, model):
        return model.get_generation_display()
    dspl_generation.short_description = _("Generation")
    dspl_generation.admin_order_field = "generation"


class CamperAdmin(PersonAdmin, PayerAdmin, MemberAdmin):
    raw_id_fields = ("counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["counselor", "mother", "father"]}
    readonly_fields = PayerAdmin._rf + MemberAdmin._rf

    fieldsets = [
        (_("Basic Info"), {"fields":
                           [("first_name", "second_name"),
                            ("first_surname", "second_surname"),
                            ("badge_name", "counselor"),
                            ("gender", "no_pay"),
                            ("structure", "generation"),
                            ("cabin", "bus"),
                            ("balance_as_currency", "amount_due")]}),
        (_("Customs"), {"classes": ("grp-collapse grp-closed",),
                        "fields":
                        [("birth_date", "registrar"),
                        ("birth_cert_num", "birth_cert_fol", "birth_cert_book"),
                        ("state", "province"),
                        "occupation",
                        "passport",
                        ("mother", "father"),
                        ("special_case", "docs_signed")]}),
    ]

    list_display = (PersonAdmin._ld + MemberAdmin._ld + PayerAdmin._ld
                    + ["docs_signed", "special_case"])
    list_editable = ["docs_signed", "special_case"]
    list_filter = MemberAdmin._lf + PayerAdmin._lf + ["docs_signed",
                                                      "special_case"]
    search_fields = (PersonAdmin._sf + MemberAdmin._sf
                     + ["counselor__first_name"] + ["counselor__second_name"]
                     + ["counselor__first_surname"]
                     + ["counselor__second_surname"])


class CounselorAdmin(PersonAdmin, PayerAdmin, MemberAdmin):
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"]}
    readonly_fields = PayerAdmin._rf + MemberAdmin._rf

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              ("badge_name", "small_group"),
              ("gender", "no_pay"),
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
              ("gender", "no_pay"),
              ("balance_as_currency", "amount_due"))

    list_display = PersonAdmin._ld + ["cabin"] + PayerAdmin._ld
    list_editable = ["cabin"]
    list_filter = PersonAdmin._lf + ["no_pay"] + ["cabin"] + PayerAdmin._lf
    search_fields = PersonAdmin._sf + ["cabin"]


class ParentAdmin(PersonAdmin, HideFromAdminList):
    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "gov_id",
              "gender",
              "birth_date",
              ("state", "province"),
              "occupation")

    list_display = PersonAdmin._ld
    list_filter = PersonAdmin._lf
    search_fields = PersonAdmin._sf

admin.site.register(Camper, CamperAdmin)
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Payment, HideFromAdminList)
