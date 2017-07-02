from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from .models import Camp, Chaperone, Lawyer


#######################
# User admin override #
#######################

class CustomUserAdmin(UserAdmin):
    """
    Add a few extra fields to the User admin.
    """
    extra_list_display = ("is_active", "is_superuser", "date_joined", "last_login")
    list_display = UserAdmin.list_display + extra_list_display


if User in admin.site._registry:
    admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


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
