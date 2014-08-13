from django.conf.urls import patterns, include, url

from django.contrib import admin

from views import Home

admin.autodiscover()
urlpatterns = patterns("",
    # Examples:
    # url(r"^$", "campmanager.views.home", name="home"),
    # url(r"^campmanager/", include("campmanager.foo.urls")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

    url(r"^grappelli/", include("grappelli.urls")),

    # Login page with redirection capabilities via "next" param
    url(r"^accounts/login/$", "django.contrib.auth.views.login",
        {"template_name": "admin/login.html"}),

    # Uncomment the next line to enable the admin:
    url(r"^staff/", include(admin.site.urls)),

    # Reports app URL patterns
    url(r"^reports/", include("reports.urls")),

    # General URLs
    url(r"^$", Home.as_view(), name="home"),
)
