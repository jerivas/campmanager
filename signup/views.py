from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from signup.models import Camper


class CamperList(ListView):
    model = Camper

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CamperList, self).dispatch(*args, **kwargs)


class CamperCreate(CreateView):
    model = Camper

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CamperCreate, self).dispatch(*args, **kwargs)


class CamperUpdate(UpdateView):
    model = Camper

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CamperUpdate, self).dispatch(*args, **kwargs)


class CamperDelete(DeleteView):
    model = Camper
    success_url = reverse_lazy('camper_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CamperDelete, self).dispatch(*args, **kwargs)
