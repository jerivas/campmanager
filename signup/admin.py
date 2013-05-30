from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from signup.models import Camper, Payment, Counselor, Parent


class PaymentInline(generic.GenericTabularInline):
    model = Payment
    extra = 1


class CamperAdmin(admin.ModelAdmin):
    inlines = (PaymentInline,)
    radio_fields = {"gender": admin.HORIZONTAL}
    raw_id_fields = ("assigned_counselor", "mother", "father")
    autocomplete_lookup_fields = {"fk": ["assigned_counselor", "mother", "father"],}
    readonly_fields = ("balance_as_currency", "amount_due")

    fieldsets = [
        (_("Basic Info"), {"fields":
                           [("first_name", "second_name"),
                           ("first_surname", "second_surname"),
                           "badge_name",
                           "gender",
                           "assigned_counselor",
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


class CounselorAdmin(admin.ModelAdmin):
    inlines = (PaymentInline,)
    radio_fields = {"gender": admin.HORIZONTAL}
    raw_id_fields = ("small_group",)
    autocomplete_lookup_fields = {"fk": ["small_group"],}
    readonly_fields = ("balance_as_currency", "amount_due")

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "badge_name",
              "gender",
              "small_group",
              ("no_pay", "balance_as_currency", "amount_due"))

    list_display = ("first_name", "second_name", "first_surname",
                    "second_surname", "small_group", "generation",
                    "structure", "fully_paid", "amount_due")
    list_display_links = ("first_name", "second_name", "first_surname",
                          "second_surname")


class ParentAdmin(admin.ModelAdmin):
    radio_fields = {"gender": admin.HORIZONTAL}

    fields = (("first_name", "second_name"),
              ("first_surname", "second_surname"),
              "gov_id",
              "gender",
              "birth_date",
              ("state", "province"),
              "occupation")

admin.site.register(Camper, CamperAdmin)
admin.site.register(Payment)
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Parent, ParentAdmin)
