from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from signup.models import Camper, Counselor, Guest, Parent, Payment
from logistics.models import SmallGroup
from finances.models import Transaction


class Permission(ListView):
    """Display multiple Camper permissions at once"""
    context_object_name = "campers"
    template_name = "reports/permission.html"

    def get_queryset(self):
        pks = self.kwargs["pks"].split(",")
        campers = []
        for pk in pks:
            try:
                c = Camper.objects.get(pk=pk)
            except Camper.DoesNotExist:
                pass
            else:
                campers.append(c)
        return campers

    @method_decorator(permission_required("signup.view_reports"))
    def dispatch(self, *args, **kwargs):
        return super(Permission, self).dispatch(*args, **kwargs)


@permission_required("finances.view_reports")
def full_financial_report(request):
    """A full report spanning Payments and Transactions"""
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
