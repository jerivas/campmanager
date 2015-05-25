from django.db.models import Q
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _


class BalanceStatusFilter(SimpleListFilter):
    """
    Allows filtering Payers according to how much of the camp's price
    they've paid so far.
    """
    title = _("Balance Status")
    parameter_name = "balance"

    def lookups(self, request, model_admin):
        return (
            ("no_pay", _("Doesn't pay")),
            ("signup", _("Signed up")),
            ("owes", _("Due payment")),
            ("full", _("Fully paid")),
            ("over", _("Overpaid")),
        )

    def queryset(self, request, queryset):
        from general.models import Camp
        camp = Camp.objects.get()  # Get the camp information

        price = camp.price
        fined_price = price + camp.fine

        if self.value() == "no_pay":
            return queryset.filter(no_pay=True)
        if self.value() == "signup":
            return queryset.filter(signed_up=True)
        if self.value() == "owes":
            return queryset.filter(
                ((Q(fined=False) & Q(balance__lt=price)) |
                 (Q(fined=True) & Q(balance__lt=fined_price))),
                signed_up=True)
        if self.value() == "full":
            return queryset.filter(
                (Q(fined=False) & Q(balance__exact=price)) |
                (Q(fined=True) & Q(balance__exact=fined_price)))
        if self.value() == "over":
            return queryset.filter(
                (Q(fined=False) & Q(balance__gt=price)) |
                (Q(fined=True) & Q(balance__gt=fined_price)))
