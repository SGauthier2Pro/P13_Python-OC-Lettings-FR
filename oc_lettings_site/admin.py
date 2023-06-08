from django.contrib import admin

from ._models import Letting
from ._models import Address
from ._models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
