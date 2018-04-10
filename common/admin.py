from django.contrib import admin
from .admins import CaveAdmin
from .models import Cave

admin.site.register(Cave, CaveAdmin)
