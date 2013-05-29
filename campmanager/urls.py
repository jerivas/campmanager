from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'campmanager.views.home', name='home'),
    # url(r'^campmanager/', include('campmanager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^staff/', include(admin.site.urls)),

    # Signup app URL patterns
    url(r"^signup/", include("signup.urls")),
)
