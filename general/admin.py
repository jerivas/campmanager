from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from .models import Camp, Chaperone, Lawyer


########
# Camp #
########

class ChaperoneInlineAdmin(admin.StackedInline):
    model = Chaperone
    radio_fields = {"gender": admin.HORIZONTAL}
    fieldsets = [
        (None, {
            "fields": [
                ("first_name", "second_name"),
                ("first_surname", "second_surname"),
                ("gov_id", "occupation"),
                ("province", "state"),
                ("birth_date", "gender"),
            ],
        }),
    ]


class LawyerInlineAdmin(admin.TabularInline):
    model = Lawyer
    extra = 1


@admin.register(Camp)
class CampAdmin(SingletonModelAdmin):
    inlines = [ChaperoneInlineAdmin, LawyerInlineAdmin]
    fieldsets = [
        (None, {
            "fields": [
                ("title", "price"),
                ("signup_fee", "fine"),
            ],
        }),
        (_("Customs"), {
            "fields": [
                ("destination", "duration"),
                ("permission_location", "permission_timestamp"),
            ],
            "classes": ["grp-collapse", "grp-closed"],
        }),
    ]

    def has_add_permission(self, request):
        """
        Only allow creation if no objects exist.
        """
        return not Camp.objects.all().exists()
