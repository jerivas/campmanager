from django.core.exceptions import FieldDoesNotExist
from django.utils.translation import ugettext


class FriendlyExportMixin:
    """
    Mixin for "friendlier" output when exporting models.
    It uses verbose names in column headers and get_XXX_display for values that support
    it. Might cause trouble when importing data back.
    https://github.com/django-import-export/django-import-export/issues/52
    """

    def get_export_headers(self):
        """
        Return column headers based on verbose_name.
        """
        headers = []
        for field in self.get_fields():
            # Split fields that traverse relations
            field_name = field.column_name.split("__")[0]
            try:
                f = self.Meta.model._meta.get_field(field_name)
            except FieldDoesNotExist:
                # This is probably a custom Field defined in the resource
                headers.append(ugettext(field.column_name))
            else:
                headers.append(ugettext(f.verbose_name))
        return headers

    def export_field(self, field, obj):
        """
        Use get_XXX_display when exporting fields that support it.
        """
        field_name = self.get_field_name(field)
        method = getattr(self, "dehydrate_%s" % field_name, None)
        if method is not None:
            return method(obj)
        else:
            display = getattr(obj, "get_%s_display" % field_name, None)
            if display:
                return display()
        return field.export(obj)
