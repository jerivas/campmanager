from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from logistics.models import SmallGroup


class SmallGroupAdmin(admin.ModelAdmin):
    """Admin class for Small Groups"""

    fields = ("title",
              ("generation", "structure"),
              ("bus", "cabin"),
              "member_list")

    readonly_fields = ["structure", "member_list"]
    list_display = ["title", "counselor", "camper_count", "dspl_structure",
        "dspl_generation", "cabin", "bus"]
    list_editable = ["cabin", "bus"]
    list_filter = ["structure", "generation", "cabin", "bus"]
    list_per_page = 15
    search_fields = ["^structure", "title", "^cabin", "^bus",
        "^counselor__first_name", "^counselor__second_name",
        "^counselor__first_surname", "^counselor__second_surname"]

    def dspl_structure(self, model):
        return model.get_structure_display()
    dspl_structure.short_description = _("Structure")
    dspl_structure.admin_order_field = "structure"

    def dspl_generation(self, model):
        return model.get_generation_display()
    dspl_generation.short_description = _("Generation")
    dspl_generation.admin_order_field = "generation"

    def camper_count(self, model):
        return model.camper_set.count()
    camper_count.short_description = _("Campers")

    def member_list(self, model):
        from django.core.urlresolvers import reverse

        m_list = ""
        for m in model.get_members():
            url_str = "admin:%s_%s_change" % (m._meta.app_label,
                m._meta.object_name.lower())
            m_url = reverse(url_str, args=[m.pk])
            m_list += ("%s: <a href='%s'>%s</a><br>" %
                       (m._meta.verbose_name.title(), m_url, m))
        return m_list
    member_list.short_description = _("Members")
    member_list.allow_tags = True

admin.site.register(SmallGroup, SmallGroupAdmin)
