from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from siterelated.admin import HiddenSiteAdminMixin

from finances.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(HiddenSiteAdminMixin, admin.ModelAdmin):
    radio_fields = {"transaction_type": admin.HORIZONTAL}
    fields = [
        ("transaction_id", "transaction_type"),
        ("transaction_date", "amount"),
        ("origin", "destination"),
        "site",
    ]
    list_display = [
        "transaction_id", "transaction_type", "amount_as_currency",
        "transaction_date", "origin", "destination"]
    list_filter = ["transaction_type"]
    list_per_page = 15
    date_hierarchy = "transaction_date"
    search_fields = ["transaction_id", "origin", "destination"]

    def amount_as_currency(self, model):
        return "$%s" % model.amount
    amount_as_currency.short_description = _("Amount")
    amount_as_currency.admin_order_field = "amount"
