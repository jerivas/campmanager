from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login

from .views import Home

urlpatterns = [

    # Grappelli admin skin
    url(r"^grappelli/", include("grappelli.urls")),

    # Login page with redirection capabilities via "next" param
    url(r"^accounts/login/$",
        login, {"template_name": "admin/login.html"}, name="login"),

    # Uncomment the next line to enable the admin:
    url(r"^staff/", include(admin.site.urls)),

    # Reports app URL patterns
    url(r"^reports/", include("reports.urls")),

    # General URLs
    url(r"^$", Home.as_view(), name="home"),
]
