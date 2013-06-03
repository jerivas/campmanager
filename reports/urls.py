from django.conf.urls import patterns, url

urlpatterns = patterns("reports.views",
    url(r"finances/$", "full_financial_report", name="full_financial_report"),
)
