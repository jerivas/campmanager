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

    class Meta:
        model = Payment
        fields = [
            "receipt_id",
            "amount",
            "payment_date",
            "notes",
        ]
        export_order = fields
