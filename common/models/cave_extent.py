from django.db import models
from .base_entity import BaseEntity
from .cave import Cave


class CaveExtent(BaseEntity):
    """ Adott barlanghoz köthető térbeli dimenzókat tároló entitás """

    hossz = models.FloatField(verbose_name='Hossz')
    vertikalis = models.FloatField(verbose_name='Vertikális kiterjedés')
    melyseg = models.FloatField(verbose_name='Mélység')
    magassag = models.FloatField(verbose_name='Magasság')
    barlang = models.ForeignKey(Cave, on_delete=models.CASCADE)
