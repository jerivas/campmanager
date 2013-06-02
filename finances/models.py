from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Transaction(models.Model):
    """A transaction related to a budget."""
    TRANSACTION_TYPE_CHOICES = (
        ("income", _("Income")),
        ("egress", _("Egress")),
    )
    transaction_id = models.CharField(_("Transaction ID"), max_length=16,
        blank=False)
    transaction_type = models.CharField(_("Type"), max_length=16, blank=False,
        choices=TRANSACTION_TYPE_CHOICES, default="income")
    transaction_date = models.DateField(_("Date"), blank=True, null=True)
    amount = models.DecimalField(_("Amount"), max_digits=6, decimal_places=2,
        blank=False)
    origin = models.CharField(_("Origin"), max_length=128, blank=True,
        null=True)
    destination = models.CharField(_("Destination"), max_length=128,
        blank=True, null=True)

    def __unicode__(self):
        return "%s - $%s (%s)" % (self.transaction_id, self.amount,
                                  self.get_transaction_type_display())

    class Meta:
        ordering = ["-transaction_date"]
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def save(self, *args, **kwargs):
        """Set default for ``transaction_date`` as now"""
        if self.transaction_date is None:
            self.transaction_date = now()
        super(Transaction, self).save(*args, **kwargs)
