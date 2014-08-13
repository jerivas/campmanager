from django.views.generic.base import TemplateView


class Home(TemplateView):
    """
    Simple placeholder for home page.
    """
    template_name = "index.html"
