from django.contrib import admin
from ..models import CaveExtent


class CaveExtentInline(admin.TabularInline):
    model = CaveExtent
    extra = 0
    fields = [
        'hossz',
        'vertikalis',
        'melyseg',
        'magassag',
        'barlang',
    ]
    ordering = ('-created', )
