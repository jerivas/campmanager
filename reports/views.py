from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from xhtml2pdf import pisa

from signup.models import Payment, Camper, Counselor, Guest
from finances.models import Transaction
from logistics.models import SmallGroup


class PDFMixin(object):
    """
    Mixin to enable PDF rendering of any view.
    Allows defining a custom template for PDF document,
    and a custom document name for the download.
    """
    pdf_filename = "document"
    pdf_template_name = None

    def get_pdf_template_name(self):
        """
        Gets the template name for the PDF.
        Fall back to the parent view template if not defined.
        """
        if self.pdf_template_name is None:
            return self.get_template_names()[0]
        return self.pdf_template_name

    def get_pdf_filename(self):
        """
        Gets the name that the generated PDF document will have.
        """
        return self.pdf_filename

    @staticmethod
    def get_timestamp():
        """
        Generates a filename-friendly timestamp.
        """
        from django.utils import timezone
        tz = timezone.get_default_timezone()
        return timezone.now().astimezone(tz).strftime("%Y-%m-%d_%H-%M-%S")

    def render_to_response(self, context, **response_kwargs):
        """
        Render the template as PDF by checking a URL parameter.
        """
        # If the format=pdf param is passed, render the PDF
        if self.request.GET.get("format") == "pdf":
            filename = self.get_pdf_filename()
            template = self.get_pdf_template_name()
            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = "attachment; filename=%s.pdf" % filename
            html = get_template(template).render(context)
            pisa.CreatePDF(html, response)
            return response
        # Else, the parent view response is returned
        return super(PDFMixin, self).render_to_response(context, **response_kwargs)


class Permission(PermissionRequiredMixin, PDFMixin, TemplateView):
    """
    Display a single or multiple Camper permissions at once.
    """
    permission_required = "signup.generate_permission"
    template_name = "reports/permission.html"

    def get_pdf_filename(self):
        return "permiso-migratorio-%s" % self.get_timestamp()

    def get_context_data(self, **kwargs):
        """
        Get all the selected Campers into the template context.
        Campers are specified via GET params.
        """
        context = super(Permission, self).get_context_data(**kwargs)

        # Handle malformed URL params
        try:
            pks = self.request.GET.get("id").split(",")
        except AttributeError:  # Catch trying to split NoneType (no "id")
            return context
        if pks == [""]:  # Deal with empty "id" parameter
            return context

        campers, omitted, total = [], 0, 0
        for pk in pks:
            try:
                camper = Camper.objects.select_related(
                    "mother", "father", "small_group").get(pk=pk)
            except (ValueError, Camper.DoesNotExist):
                continue
            if camper.permission_status in [Camper.SPECIAL, Camper.INCOMPLETE]:
                omitted += 1
            else:
                campers.append(camper)
            total += 1

        context.update({
            "campers": campers,
            "omitted": omitted,
            "total": total,
        })
        return context


class CabinReport(PermissionRequiredMixin, PDFMixin, ListView):
    """
    Generates a list of the Small Groups that will occupy a Cabin.
    """
    permission_required = "logistics.view_reports"
    template_name = "reports/cabin_report.html"
    context_object_name = "small_groups"
    queryset = SmallGroup.objects.select_related("counselor").order_by(
        "cabin", "generation")

    def get_pdf_filename(self):
        return "reporte-de-cabanas-%s" % self.get_timestamp()


class BusReport(PermissionRequiredMixin, PDFMixin, ListView):
    """
    Generates a list of Small Groups in each Bus.
    """
    permission_required = "logistics.view_reports"
    template_name = "reports/bus_report.html"
    context_object_name = "small_groups"
    queryset = SmallGroup.objects.select_related("counselor").order_by(
        "bus", "generation")

    def get_pdf_filename(self):
        return "reporte-de-buses-%s" % self.get_timestamp()


class AttendantReport(PermissionRequiredMixin, PDFMixin, TemplateView):
    """
    Displays all attendants: members of Small Groups and Guests.
    """
    permission_required = "logistics.attendant_report"
    template_name = "reports/attendant_report.html"

    def get_pdf_filename(self):
        return "reporte-de-asistencia-%s" % self.get_timestamp()

    def get_context_data(self, **kwargs):
        context = super(AttendantReport, self).get_context_data(**kwargs)
        counselors = Counselor.objects.filter(signed_up=True).count()
        campers = Camper.objects.filter(signed_up=True).count()
        context.update({
            "total": counselors + campers,
            "small_groups": SmallGroup.objects.select_related(),
            "guests": Guest.objects.filter(signed_up=True),
        })
        return context


class FinancesReport(PermissionRequiredMixin, PDFMixin, TemplateView):
    """
    A full report spanning Payments and Transactions.
    """
    permission_required = "finances.view_reports"
    template_name = "reports/finances_report.html"

    def get_pdf_filename(self):
        return "reporte-financiero-%s" % self.get_timestamp()

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

        context.update({
            "transaction_income": transaction_income,
            "transaction_egress": transaction_egress,
            "payments_income": payments_income,
            "income_count": income_count,
            "egress_count": egress_count,
            "payment_count": payment_count,
            "total": total
        })
        return context
