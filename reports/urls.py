from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    Permission, CabinReport, BusReport, AttendantReport, FinancesReport)

urlpatterns = [
    url(r"^permission/$", Permission.as_view(), name="permission"),
    url(r"^cabins/$", CabinReport.as_view(), name="cabin_report"),
    url(r"^buses/$", BusReport.as_view(), name="bus_report"),
    url(r"^attendants/$", AttendantReport.as_view(), name="attendant_report"),
    url(r"^finances/$", FinancesReport.as_view(), name="finances_report"),
]
