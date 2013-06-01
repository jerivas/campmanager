from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from logistics.models import SmallGroup


class SmallGroupAdmin(admin.ModelAdmin):
    """Admin class for Small Groups"""

    fields = ("title",
              ("generation", "structure"),
              ("bus", "cabin"))

    readonly_fields = ["structure"]
    list_display = ["title", "dspl_structure", "dspl_generation",
        "dspl_cabin", "dspl_bus"]
    list_filter = ["structure", "generation", "cabin", "bus"]
    search_fields = ["structure", "title", "cabin", "bus"]

    def dspl_structure(self, model):
        return model.get_structure_display()
    dspl_structure.short_description = _("Structure")
    dspl_structure.admin_order_field = "structure"

    def dspl_generation(self, model):
        return model.get_generation_display()
    dspl_generation.short_description = _("Generation")
    dspl_generation.admin_order_field = "generation"

    def dspl_cabin(self, model):
        return model.get_cabin_display() or "----"
    dspl_cabin.short_description = _("Cabin")
    dspl_cabin.admin_order_field = "cabin"

    def dspl_bus(self, model):
        return model.get_bus_display() or "----"
    dspl_bus.short_description = _("Bus")
    dspl_bus.admin_order_field = "bus"

admin.site.register(SmallGroup, SmallGroupAdmin)
