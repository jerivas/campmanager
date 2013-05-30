from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from logistics.models import SmallGroup, Generation

admin.site.register(SmallGroup)
admin.site.register(Generation)
