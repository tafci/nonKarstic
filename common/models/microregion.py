from django.db import models
from django.contrib.gis.db import models as gis_models
from .base_entity import BaseEntity
from .region import Region


class Microregion(BaseEntity):
    """ Kistájegység adatait reprezentáló entitás """

    nev = models.CharField(max_length=255, verbose_name='Név', help_text='Kistáj neve')
    kod = models.CharField(max_length=255, verbose_name='Kód', help_text='Kistáj kódja')
    nagytaj = models.ForeignKey(Region, on_delete=models.CASCADE)
    geom = gis_models.MultiPolygonField()

    def __str__(self):
        return self.nev

    class Meta:
        ordering = ['nev']
