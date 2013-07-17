from django.conf.urls import patterns, url

from reports.views import Permission, CabinReport

urlpatterns = patterns("reports.views",
    url(r"^finances/$", "full_financial_report", name="full_financial_report"),
    url(r"^permission/$", Permission.as_view(), name="permission"),
    url(r"^cabins/$", CabinReport.as_view(), name="cabin_report"),
)
