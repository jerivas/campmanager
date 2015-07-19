from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from logistics.models import SmallGroup


class SmallGroupAdmin(admin.ModelAdmin):
    """Admin class for Small Groups"""

    fields = ("title",
              ("generation", "structure"),
              ("bus", "cabin"),
              "member_list")

    readonly_fields = ["structure", "member_list"]
    list_display = ["title", "signed_up_count", "structure",
        "generation", "cabin", "bus"]
    list_editable = ["cabin", "bus"]
    list_filter = ["structure", "generation", "cabin", "bus"]
    search_fields = ["^structure", "title", "^cabin", "^bus",
        "^counselor__first_name", "^counselor__second_name",
        "^counselor__first_surname", "^counselor__second_surname",
        "^counselor__badge_name"]

    def signed_up_count(self, model):
        signed_up = len(model.get_members(signed_up=True))
        total = len(model.get_members())
        return "%s / %s" % (signed_up, total)
    signed_up_count.short_description = _("Signed up members")

    def member_list(self, model):
        m_list = ""
        for m in model.get_members():
            url_str = "admin:%s_%s_change" % (m._meta.app_label,
                m._meta.object_name.lower())
            m_url = reverse(url_str, args=[m.pk])
            m_signed_up = _("Signed up") if m.signed_up else _("Not signed up")
            m_list += ("%s: <a href='%s'>%s</a> (%s)<br>" %
                       (m._meta.verbose_name.title(), m_url, m, m_signed_up))
        return m_list
    member_list.short_description = _("Members")
    member_list.allow_tags = True

admin.site.register(SmallGroup, SmallGroupAdmin)
