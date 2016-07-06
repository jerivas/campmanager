from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from logistics.models import SmallGroup


@admin.register(SmallGroup)
class SmallGroupAdmin(admin.ModelAdmin):
    fields = [
        "title",
        ("generation", "structure"),
        ("bus", "cabin"),
        "member_list"
    ]

    list_select_related = ["counselor"]
    list_prefetch_related = ["camper_set"]
    list_display = [
        "title", "signed_up_count", "structure", "generation", "cabin", "bus"]
    list_editable = ["cabin", "bus"]
    list_filter = ["structure", "generation", "cabin", "bus"]
    readonly_fields = ["structure", "member_list"]
    search_fields = [
        "^structure", "title", "^cabin", "^bus", "^counselor__first_name",
        "^counselor__second_name", "^counselor__first_surname",
        "^counselor__second_surname", "^counselor__badge_name"]

    def signed_up_count(self, model):
        signed_up = len(model.get_members(signed_up=True))
        total = len(model.get_members())
        return "%s / %s" % (signed_up, total)
    signed_up_count.short_description = _("Signed up members")

    def member_list(self, small_group):
        """
        Generate links to the admin change form of the individual members.
        """
        def _get_member_data(member):
            meta = member._meta
            url_name = "admin:%s_%s_change" % (meta.app_label, meta.object_name.lower())
            url = reverse(url_name, args=[member.pk])
            signed_up = _("Signed up") if member.signed_up else _("Not signed up")
            return meta.verbose_name.title(), url, member, signed_up

        member_data = map(_get_member_data, small_group.get_members())
        return format_html_join("", "{}: <a href='{}'>{}</a> ({})<br/>", member_data)
    member_list.short_description = _("Members")
