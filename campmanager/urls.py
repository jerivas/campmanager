from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from general import views

urlpatterns = [
    # Grappelli admin skin
    url(r"^grappelli/", include("grappelli.urls")),
    # Override the login view to use the admin template
    url(
        r"^accounts/login/$",
        auth_views.login,
        {"template_name": "admin/login.html"},
        name="login",
    ),
    # Grappelli looks for a pattern named "admin_password_reset" to display the
    # "Forgot your password?" link in the login form
    url(
        r"^accounts/password_reset/$",
        auth_views.password_reset,
        name="admin_password_reset",
    ),
    # Profiles are not implemented. Let's redirect to the admin.
    url(r"^accounts/profile/$", RedirectView.as_view(pattern_name="admin:index")),
    # Include the rest of the auth URLs normally
    url(r"^accounts/", include("django.contrib.auth.urls")),
    # Uncomment the next line to enable the admin:
    url(r"^staff/", include(admin.site.urls)),
    # Reports app URL patterns
    url(r"^reports/", include("reports.urls")),
    # General URLs
    url(r"^$", views.CampOverview.as_view(), name="home"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
