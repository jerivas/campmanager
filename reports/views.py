from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from xhtml2pdf import pisa

from signup.models import Payment, Camper, Counselor, Guest
from finances.models import Transaction
from logistics.models import SmallGroup


class PDFMixin(object):
    """
    Allows rendering any template as PDF.
    Child classes must implement the pdf_template_name attribute.
    """

    def get_pdf_name(self, request, *args, **kwargs):
        """
        Gets the name that the final PDF document will have.
        """
        try:
            return self.pdf_name
        except AttributeError:
            return "document"

    def get(self, request, *args, **kwargs):
        """
        Render the template as PDF by checking a URL parameter.
        """
        if request.GET.get("format") == "pdf":
            context = self.get_context_data(**kwargs)
            response = HttpResponse(content_type="application/pdf")
            name = self.get_pdf_name(request)
            response["Content-Disposition"] = "attachment; filename=%s.pdf" % name
            html = get_template(self.pdf_template_name).render(context)
            pisa.CreatePDF(html, response)
            return response
        return super(PDFMixin, self).get(request, *args, **kwargs)


class Permission(PDFMixin, TemplateView):
    """
    Display a single or multiple Camper permissions at once.
    """
    template_name = "reports/permission.html"
    pdf_template_name = "reports/pdf_permission.html"

    def get_pdf_name(self, request, *args, **kwargs):
        """
        Name each PDF with a timestamp.
        """
        from datetime import datetime
        return str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))

    def get_context_data(self, **kwargs):
        """
        Get all the selected Campers into the template context.
        """
        context = super(Permission, self).get_context_data(**kwargs)
        context["campers"] = []  # Empty list to hold campers
        context.update(dict.fromkeys(
            # Set this counters to zero
            ["omitted", "total"], 0))
        try:
            pks = self.request.GET.get("id").split(",")
        except AttributeError:  # Catch trying to split NoneType (no "id")
            return context
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
                        # Otherwise, append camper to "campers" list
                        context["campers"].append(c)
                    # Count all requested permissions, omitted or not.
                    context["total"] += 1
        return context

    @method_decorator(permission_required("signup.generate_permission"))
    def dispatch(self, *args, **kwargs):
        return super(Permission, self).dispatch(*args, **kwargs)


class CabinReport(ListView):
    """Generates a list of Small Groups in each Cabin."""
    template_name = "reports/cabin_report.html"
    context_object_name = "small_groups"
    queryset = SmallGroup.objects.select_related("counselor").order_by(
        "cabin", "generation")

    @method_decorator(permission_required("logistics.view_reports"))
    def dispatch(self, *args, **kwargs):
        return super(CabinReport, self).dispatch(*args, **kwargs)


class BusReport(ListView):
    """Generates a list of Small Groups in each Bus."""
    template_name = "reports/bus_report.html"
    context_object_name = "small_groups"
    queryset = SmallGroup.objects.select_related("counselor").order_by(
        "bus", "generation")

    @method_decorator(permission_required("logistics.view_reports"))
    def dispatch(self, *args, **kwargs):
        return super(BusReport, self).dispatch(*args, **kwargs)


class AttendantReport(TemplateView):
    """Displays all attendants, members of Small Groups and Guests."""
    template_name = "reports/attendant_report.html"

    def get_context_data(self, **kwargs):
        c = super(AttendantReport, self).get_context_data(**kwargs)
        counselors = Counselor.objects.filter(signed_up=True).count()
        campers = Camper.objects.filter(signed_up=True).count()
        c["total"] = counselors + campers
        c["small_groups"] = SmallGroup.objects.select_related()
        c["guests"] = Guest.objects.filter(signed_up=True)
        return c

    @method_decorator(permission_required("logistics.attendant_report"))
    def dispatch(self, *args, **kwargs):
        return super(AttendantReport, self).dispatch(*args, **kwargs)


class FinancesReport(TemplateView):
    """A full report spanning Payments and Transactions."""
    template_name = "reports/finances_report.html"

    def get_context_data(self, **kwargs):
        context = super(FinancesReport, self).get_context_data(**kwargs)
        payments_income = sum(p.amount for p in Payment.objects.all())
        payment_count = Payment.objects.count()
        incomes = Transaction.objects.filter(transaction_type="income")
        transaction_income = sum(i.amount for i in incomes)
        income_count = incomes.count()
        egresses = Transaction.objects.filter(transaction_type="egress")
        transaction_egress = sum(e.amount for e in egresses)
        egress_count = egresses.count()
        total = payments_income + transaction_income - transaction_egress
        context = {"transaction_income": transaction_income,
            "transaction_egress": transaction_egress,
            "payments_income": payments_income, "income_count": income_count,
            "egress_count": egress_count, "payment_count": payment_count,
            "total": total}
        return context

    @method_decorator(permission_required("finances.view_reports"))
    def dispatch(self, *args, **kwargs):
        return super(FinancesReport, self).dispatch(*args, **kwargs)
