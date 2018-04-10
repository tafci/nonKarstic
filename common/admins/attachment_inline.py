from django.contrib import admin
from ..models import Attachment


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0
    fields = [
        'cim',
        'leiras',
        'attachment',
        'tipus',
        'barlang',
    ]
    ordering = ('created', )
