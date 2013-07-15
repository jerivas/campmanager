from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from signup.models import Camper, Payment
from finances.models import Transaction


class Permission(TemplateView):
    """Display multiple Camper permissions at once."""
    template_name = "reports/permission.html"

    def get_context_data(self, **kwargs):
        """
        Filter out and categorize Campers according to their permission
        status. Also, update Campers if their permission is being printed
        for the first time.
        """
        context = super(Permission, self).get_context_data(**kwargs)
        context["campers"] = []  # Empty list to hold campers
        context.update(dict.fromkeys(
            # Set this counters to zero
            ["omitted", "first_print", "reprint", "total"], 0))
        try:
            pks = self.request.GET.get("id").split(",")
        except AttributeError:  # Catch trying to split NoneType (no "id")
            pass
        if pks == [""]:  # Deal with empty "id" parameter
            pass
        else:
            for pk in pks:
                try:
                    c = Camper.objects.select_related("mother", "father",
                        "small_group").get(pk=pk)
                except Camper.DoesNotExist:
                    pass
                else:
                    # Special cases or incomplete docs are added to the
                    # "omitted" count, but not to the "campers" list.
                    if (c.permission_status == Camper.SPECIAL or
                        c.permission_status == Camper.INCOMPLETE):
                        context["omitted"] += 1
                    else:
                        # Ready to print are bumbped up to "printed".
                        if c.permission_status == Camper.TO_PRINT:
                            c.permission_status = Camper.PRINTED
                            c.save()
                            context["first_print"] += 1
                        else:
                            context["reprint"] += 1
                        # Append camper to "campers" list if it's a first
                        # print or reprint.
                        context["campers"].append(c)
                    # Count all requested permissions, omitted or not.
                    context["total"] += 1
        return context

    @method_decorator(permission_required("signup.generate_permission"))
    def dispatch(self, *args, **kwargs):
        return super(Permission, self).dispatch(*args, **kwargs)


@permission_required("finances.view_reports")
def full_financial_report(request):
    """A full report spanning Payments and Transactions."""
    template = "reports/full_financial_report.html"
    payments_income = sum(p.amount for p in Payment.objects.all())
    payment_count = Payment.objects.count()
    incomes = Transaction.objects.filter(transaction_type="income")
    transaction_income = sum(i.amount for i in incomes)
    income_count = incomes.count()
    egresses = Transaction.objects.filter(transaction_type="egress")
    transaction_egress = sum(e.amount for e in egresses)
    egress_count = egresses.count()
    total = payments_income + transaction_income - transaction_egress
    context = {"transaction_income": transaction_income, "transaction_egress":
               transaction_egress, "payments_income": payments_income,
               "income_count": income_count, "egress_count": egress_count,
               "payment_count": payment_count, "total": total}
    return render(request, template, context)
