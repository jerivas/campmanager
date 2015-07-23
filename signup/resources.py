from import_export import resources

from utils.resources import FriendlyExportMixin
from .models import Camper, Payment, Counselor, Guest


class CamperResource(FriendlyExportMixin, resources.ModelResource):

    class Meta:
        model = Camper
        fields = [
            "first_name", "second_name", "first_surname", "second_surname", "structure",
            "generation", "small_group__title", "counselor__badge_name", "signed_up",
            "fined", "balance", "permission_status"
        ]
        export_order = fields


class CounselorResource(FriendlyExportMixin, resources.ModelResource):

    class Meta:
        model = Counselor
        fields = [
            "first_name", "second_name", "first_surname", "second_surname", "structure",
            "generation", "small_group__title", "signed_up", "fined", "balance"
        ]
        export_order = fields


class GuestResource(FriendlyExportMixin, resources.ModelResource):

    class Meta:
        model = Guest
        fields = [
            "first_name", "second_name", "first_surname", "second_surname", "signed_up",
            "fined", "balance", "cabin"
        ]
        export_order = fields


class PaymentResource(FriendlyExportMixin, resources.ModelResource):

    class Meta:
        model = Payment
        fields = ["receipt_id", "amount", "payment_date", "notes"]
        export_order = fields
