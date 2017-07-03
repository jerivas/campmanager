from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from siterelated.models import SiteRelated


@python_2_unicode_compatible
class Transaction(SiteRelated):
    """
    A generic transaction for bookeeping.
    """
    TRANSACTION_TYPE_CHOICES = (
        ("income", _("Income")),
        ("egress", _("Egress")),
    )
    transaction_id = models.CharField(_("Transaction ID"), max_length=16, blank=True)
    transaction_type = models.CharField(
        _("Type"), max_length=16, blank=False, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField(_("Date"), default=now)
    amount = models.DecimalField(_("Amount"), max_digits=6, decimal_places=2, blank=False)
    origin = models.CharField(_("Origin"), max_length=128, blank=True)
    destination = models.CharField(_("Destination"), max_length=128, blank=True)

    def __str__(self):
        return "%s - $%0.2f (%s)" % (
            self.transaction_id, self.amount, self.get_transaction_type_display())

    class Meta:
        ordering = ["-transaction_id"]
        unique_together = ("site", "transaction_id")
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        permissions = (("view_reports", "View Reports"),)
