from django.conf.urls import patterns, url

from reports.views import (Permission, CabinReport, BusReport, BadgeReport,
    FinancesReport)

urlpatterns = patterns("",
    url(r"^permission/$", Permission.as_view(), name="permission"),
    url(r"^cabins/$", CabinReport.as_view(), name="cabin_report"),
    url(r"^buses/$", BusReport.as_view(), name="bus_report"),
    url(r"^badges/$", BadgeReport.as_view(), name="badge_report"),
    url(r"^finances/$", FinancesReport.as_view(), name="finances_report"),
)
