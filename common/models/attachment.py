from django.db import models
from .base_entity import BaseEntity
from .cave import Cave


class Attachment(BaseEntity):
    """ Csatolmány adatait reprezentáló entitás """

    ATTACHMENT_TYPES = (
        ('PIC', 'Fénykép'),
        ('MAP', 'Térkép'),
        ('VEC', 'Vektoros állomány'),
        ('DOC', 'Dokumentum'),
    )

    cim = models.CharField(max_length=255, verbose_name='Cím', help_text='A csatolmány elnevezése')
    leiras = models.TextField(verbose_name='Leírás', help_text='A csatolmány szöveges leírása')
    attachment = models.FileField(verbose_name='Csatolmány')
    tipus = models.CharField(max_length=3, choices=ATTACHMENT_TYPES, verbose_name='Csatolmány típusa')
    barlang = models.ForeignKey(Cave, on_delete=models.CASCADE)

    def __str__(self):
        return self.cim

    class Meta:
        ordering = ['cim', 'tipus']
