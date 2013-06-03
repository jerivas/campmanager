from django.shortcuts import render

from signup.models import Camper, Counselor, Guest, Parent, Payment
from logistics.models import SmallGroup
from finances.models import Transaction


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
