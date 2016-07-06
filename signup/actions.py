from django.db.models import F
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from signup.models import Camper


def _move_permission(modeladmin, request, queryset, forward):
    """
    Helper function for moving the permission status in any given direction.
    Checks for lower and upper limits. See all permission choices in
    signup.models module.
    """
    boundary = Camper.PROOFREAD if forward else Camper.INCOMPLETE
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
    return HttpResponseRedirect("%s?id=%s" % (url, ",".join(selected)))
generate_permission.short_description = _("Generate Permission")
