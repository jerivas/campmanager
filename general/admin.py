from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import Camp, Chaperone, Lawyer


class ChaperoneInlineAdmin(admin.StackedInline):
    model = Chaperone
    radio_fields = {"gender": admin.HORIZONTAL}
    fieldsets = (
        (None, {"fields":
         (("first_name", "second_name"), ("first_surname", "second_surname"),
          ("gov_id", "occupation"), ("province", "state"),
          ("birth_date", "gender"))
        }),
    )


class LawyerInlineAdmin(admin.TabularInline):
    model = Lawyer
    extra = 1


class CampAdmin(SingletonModelAdmin):
    inlines = [ChaperoneInlineAdmin, LawyerInlineAdmin]
    fieldsets = (
        (None, {"fields":
         ("title", ("destination", "duration"),
          ("permission_location", "permission_timestamp"))
        }),
    )

    def has_add_permission(self, request):
        """
        Only allow creation if no objects exist.
        """
        return not Camp.objects.all().exists()

admin.site.register(Camp, CampAdmin)
