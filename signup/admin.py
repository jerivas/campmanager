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

    fieldsets = [
        (_("Basic Info"), {"fields":
                            [("first_name", "second_name"),
                            ("first_surname", "second_surname"),
                            "badge_name",
                            "gender",
                            "assigned_counselor",
                            "no_pay"]}),
        (_("Customs"), {"classes": ("collapse",),
                        "fields": [("special_case", "docs_signed"), "birth_date",
                        ("state", "province"), "occupation", "passport",
                        ("birth_cert_num", "birth_cert_fol", "birth_cert_book",
                         "registrar"), "mother", "father"]}),
    ]

admin.site.register(Camper, CamperAdmin)
admin.site.register(Payment)
admin.site.register(Counselor)
admin.site.register(Parent)
