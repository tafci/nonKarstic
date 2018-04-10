from django.db import models
from django.contrib.gis.db import models as gis_models
from .base_entity import BaseEntity


class County(BaseEntity):
    """ Megye entitás """

    nev = models.CharField(max_length=255, verbose_name='Név')
    geom = gis_models.MultiPolygonField()

    def __str__(self):
        return self.nev

    class Meta:
        ordering = ['nev']
