from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from logistics.models import SmallGroup, Cabin, Generation, Bus

admin.site.register(SmallGroup)
admin.site.register(Cabin)
admin.site.register(Bus)
admin.site.register(Generation)
