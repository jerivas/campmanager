from django import forms
from django.utils.translation import ugettext_lazy as _


class CamperForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(CamperForm, self).clean()
        special_case = cleaned_data.get("special_case")
        perm_printed = cleaned_data.get("perm_printed")
        perm_signed = cleaned_data.get("perm_signed")

        if special_case and perm_printed:
            msg = _("Special cases cannot have 'Permission Printed' status.")
            self._errors["perm_printed"] = self.error_class([msg])
            del cleaned_data["perm_printed"]
        elif special_case and perm_signed:
            msg = _("Special cases cannot have 'Permission Signed' status.")
            self._errors["perm_signed"] = self.error_class([msg])
            del cleaned_data["perm_signed"]
        elif perm_signed and not perm_printed:
            msg = _("Cannot set 'Permission Signed' without first setting "
                    "'Permission Printed'.")
            self._errors["perm_signed"] = self.error_class([msg])
            del cleaned_data["perm_signed"]

        return cleaned_data
