from django.contrib.admin import SimpleListFilter
from django.conf import settings
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
            ("full", _("Fully paid")),
            ("over", _("Overpaid")),
        )

    def queryset(self, request, queryset):
        price = settings.CAMP_PRICE
        signup = settings.SIGNUP_FEE
        if self.value() == "no_pay":
            return queryset.filter(no_pay=True)
        if self.value() == "signup":
            return queryset.filter(balance__gte=signup)
        if self.value() == "full":
            return queryset.filter(balance__exact=price)
        if self.value() == "over":
            return queryset.filter(balance__gt=price)
