from django.contrib import admin

from lettings.models.letting import Letting
from lettings.models.address import Address
from profiles.models.profile import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
