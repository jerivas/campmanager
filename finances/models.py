from django.db import models
from django.utils.translation import ugettext_lazy as _


class Transaction(models.Model):
    """A transaction related to a budget."""
    TYPE_CHOICES = (
        ("income", _("Income")),
        ("egress", _("Egress")),
    )
    transaction_id = models.CharField(_("Transaction ID"), max_length=16,
                     blank=False)
    transaction_type = models.CharField(_("Type"), max_length=16, blank=False,
                       choices=TYPE_CHOICES, default="income")
    transaction_date = models.DateField(_("Date"), blank=False)
    amount = models.DecimalField(_("Amount"), max_digits=6,
             decimal_places=2, blank=False)
    origin = models.CharField(_("Origin"), max_length=128, blank=False)
    destination = models.CharField(_("Destination"), max_length=128,
                  blank=False)

    def __unicode__(self):
        return "%s - $%s (%s)" % (self.transaction_id, self.amount,
                                  self.transaction_type)

    class Meta:
        ordering = ["-transaction_date"]
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
