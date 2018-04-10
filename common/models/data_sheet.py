from django.db import models
from .base_entity import BaseEntity
from .cave import Cave


class DataSheet(BaseEntity):
    """ Barlang kutatási adatlapjának adatait reprezentáló entitás """

    ev = models.DateField(verbose_name='Kutatás éve')
    feltaras = models.BooleanField(
        verbose_name='Feltárás',
        help_text='A kutatás során történt-e feltárás')
    geologia = models.BooleanField(verbose_name='Geológia', help_text='Történt-e geológiai feltárás')
    morfologia = models.BooleanField(verbose_name='Morfológia', help_text='Történt-e morfológiai kutatás')
    hidrologia = models.BooleanField(verbose_name='Hidrológia', help_text='Történt-e hidrológiai kutatás')
    klima = models.BooleanField(verbose_name='Klíma', help_text='Történt-e klimatológiai kutatás')
    radon = models.BooleanField(verbose_name='Radon', help_text='Történt-e radon szint mérés')
    vedelem = models.BooleanField(verbose_name='Védelem', help_text='Történt-e barlang védelem kiépítés')
    geofizika = models.BooleanField(verbose_name='Geofizika', help_text='Történt-e geofizikai kutatás')
    oslenytan = models.BooleanField(verbose_name='Őslénytan', help_text='Történt-e őslénytani kutatás')
    regeszet = models.BooleanField(verbose_name='Régészet', help_text='Történt-e régészeti feltárás')
    biologia = models.BooleanField(verbose_name='Biológia', help_text='Történt-e biológiai kutatás')
    denever = models.BooleanField(verbose_name='Denevér', help_text='Történt-e denevérszámlálás')
    terkep = models.BooleanField(verbose_name='Térkép', help_text='Történt-e térképezés')
    foto = models.BooleanField(verbose_name='Fotó', help_text='Készült-e fénykép')
    leiras = models.BooleanField(verbose_name='Leírás', help_text='Készült-e vagy módosult-e a barlang leírása')
    barlang = models.ForeignKey(Cave, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-ev']
