from django.conf.urls import patterns, url
from signup.views import *

urlpatterns = patterns("",
    url(r"^$", CamperList.as_view(), name="camper_list"),
    url(r"add/$", CamperCreate.as_view(), name="camper_add"),
    url(r"(?P<pk>\d+)/update$", CamperUpdate.as_view(), name="camper_update"),
    url(r"(?P<pk>\d+)/delete/$", CamperDelete.as_view(), name="camper_delete"),
)
