"""
Resource definitions for models in the Singup app.
These classes control the content and behavior of django-import-export.
In theory they should work for both importing and exporting,
but they have only ever been used to export from the admin.
"""

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from import_export import resources
from import_export.fields import Field

from utils.resources import FriendlyExportMixin
from .models import Camper, Payment, Payer, Counselor, Guest


class PayerResource(resources.ModelResource):
    """
    Define custom fields to include methods of the Payer base model.
    Camper, Counselor, and Guest should be compatible with this.
    """
    amount_due = Field()
    amount_due.column_name = Payer.amount_due.short_description

    def dehydrate_amount_due(self, payer):
        """
        Proxy method that just calls the model method we want.
        """
        return payer.amount_due()


class CamperResource(FriendlyExportMixin, PayerResource):

    class Meta:
        model = Camper
        fields = [
            "first_name",
            "second_name",
            "first_surname",
            "second_surname",
            "has_medical_record",
            "structure",
            "generation",
            "small_group__title",
            "counselor__badge_name",
            "signed_up",
            "fined",
            "balance",
            "amount_due",
            "permission_status",
        ]
        export_order = fields


class CounselorResource(FriendlyExportMixin, PayerResource):

    class Meta:
        model = Counselor
        fields = [
            "first_name",
            "second_name",
            "first_surname",
            "second_surname",
            "has_medical_record",
            "structure",
            "generation",
            "small_group__title",
            "signed_up",
            "fined",
            "balance",
            "amount_due",
        ]
        export_order = fields


class GuestResource(FriendlyExportMixin, PayerResource):

    class Meta:
        model = Guest
        fields = [
            "first_name",
            "second_name",
            "first_surname",
            "second_surname",
            "has_medical_record",
            "cabin",
            "signed_up",
            "fined",
            "balance",
            "amount_due",
        ]
        export_order = fields


class PaymentResource(FriendlyExportMixin, resources.ModelResource):
    payer_name = Field()
    payer_name.column_name = _("Paid by")

    def dehydrate_payer_name(self, payment):
        """
        Get the representation of the person that made the payment
        via the generic relation.
        """
        return str(payment.content_object)

    class Meta:
        model = Payment
        fields = [
            "receipt_id",
            "amount",
            "payment_date",
            "notes",
            "payer_name",
        ]
        export_order = fields
