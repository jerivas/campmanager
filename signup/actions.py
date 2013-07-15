from django.db.models import F
from django.utils.translation import ugettext_lazy as _

from signup.models import Camper


def _move_permission(forward, modeladmin, request, queryset):
    boundary = Camper.SIGNED if forward else Camper.INCOMPLETE
    special = Camper.SPECIAL
    increment = 1 if forward else -1
    queryset = queryset.exclude(permission_status=boundary).exclude(
        permission_status=special)
    rows_updated = queryset.update(permission_status=F(
        "permission_status")+increment)
    if rows_updated == 0:
        modeladmin.message_user(request, _("No Campers were updated."))
    else:
        if rows_updated == 1:
            msg = _("one Camper")
        else:
            msg = _("%s Campers") % rows_updated
        modeladmin.message_user(request, _(
            "The permission status of %s was updated.") % msg)


def move_permission_forward(modeladmin, request, queryset):
    return _move_permission(True, modeladmin, request, queryset)
move_permission_forward.short_description = _(
    "Move permission status forward")


def move_permission_backwards(modeladmin, request, queryset):
    return _move_permission(False, modeladmin, request, queryset)
move_permission_backwards.short_description = _(
    "Move permission status backwards")
