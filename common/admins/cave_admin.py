from django.contrib import admin
from datetime import datetime
from .data_sheet_inline import DataSheetInline
from .cave_extent_inline import CaveExtentInline
from .attachment_inline import AttachmentInline


class CaveAdmin(admin.ModelAdmin):
    list_display = ('kataszteri_szam', 'nev', 'created', 'creater', 'updated', 'updater')
    list_filter = ('kozet', 'vedettseg', 'lathatosag', 'illetekes_np')
    fields = [
        'nev',
        'szinonimak',
        'kataszteri_szam',
        'leiras',
        'kozet',
        'vedettseg',
        'lathatosag',
        'illetekes_np',
        ('eov_x', 'eov_y'),
        'geom',
    ]
    inlines = [DataSheetInline, CaveExtentInline, AttachmentInline, ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creater = request.user
            obj.created = datetime.now()
        obj.updater = request.user

        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            instance.creater = request.user
            instance.created = datetime.now()
            instance.updater = request.user
            instance.save()
        formset.save_m2m()
