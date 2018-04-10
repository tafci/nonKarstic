from django.db import models
from .base_entity import BaseEntity


class Region(BaseEntity):
    """ Nagytájegység entitás """

    nev = models.CharField(max_length=255, verbose_name='Név')

    def __str__(self):
        return self.nev

    class Meta:
        ordering = ['nev']
