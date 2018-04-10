from django.contrib import admin
from ..models import DataSheet


class DataSheetInline(admin.TabularInline):
    model = DataSheet
    extra = 0
    fields = [
        'ev',
        'feltaras',
        'geologia',
        'morfologia',
        'hidrologia',
        'klima',
        'radon',
        'vedelem',
        'geofizika',
        'oslenytan',
        'regeszet',
        'biologia',
        'denever',
        'terkep',
        'foto',
        'leiras',
        'barlang',
    ]
    ordering = ('-created', )
