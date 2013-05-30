from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from finances.models import Budget, Transaction

admin.site.register(Budget)
admin.site.register(Transaction)
