from __future__ import unicode_literals

from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


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
