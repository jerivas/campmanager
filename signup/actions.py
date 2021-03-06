from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from signup.models import Camper


def _move_permission(modeladmin, request, queryset, forward):
    """
    Helper function for moving the permission status in any given direction.
    Checks cases where permissions should not be updated. See all permission choices
    in signup.models.Camper.
    """
    # Determine which permission status should not be modified
    LAST = Camper.PERMISSION_STATUS[-1][1][-1][0]
    FIRST = Camper.PERMISSION_STATUS[0][1][0][0]
    if forward:
        nonmovable = [LAST, Camper.PROOFREAD, Camper.SPECIAL]
    else:
        nonmovable = [FIRST, Camper.SPECIAL, Camper.PENDING_ID]

    # Move the permissions in the selected rows
    increment = 1 if forward else -1
    queryset = queryset.exclude(permission_status__in=nonmovable)
    rows_updated = queryset.update(permission_status=F("permission_status") + increment)
    if rows_updated == 0:
        modeladmin.message_user(request, _("No Campers were updated."))
    else:
        if rows_updated == 1:
            msg = _("one Camper")
        else:
            msg = _("%s Campers") % rows_updated
        modeladmin.message_user(
            request, _("The permission status of %s was updated.") % msg
        )


def move_permission_forward(modeladmin, request, queryset):
    return _move_permission(modeladmin, request, queryset, forward=True)


move_permission_forward.short_description = _("Move permission status forward")


def move_permission_backwards(modeladmin, request, queryset):
    return _move_permission(modeladmin, request, queryset, forward=False)


move_permission_backwards.short_description = _("Move permission status backwards")


def generate_permission(modeladmin, request, queryset):
    """
    Calls the permission generation view, passing all selected campers as
    URL parameters.
    """
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    url = reverse("permission")
    return HttpResponseRedirect("{}?id={}".format(url, ",".join(selected)))


generate_permission.short_description = _("Generate Permission")
