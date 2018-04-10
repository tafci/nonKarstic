from django.db import models
from django.contrib.gis.db import models as gis_models
from .base_entity import BaseEntity

SOUNDING_ROCK = (
    (10, 'Andezit'),
    (20, 'Andezittufa'),
    (30, 'Bazalt'),
    (40, 'Bazalttufa'),
    (50, 'Bazalttufit'),
    (60, 'Dácit'),
    (70, 'Gránit'),
    (80, 'Gránitporfír'),
    (90, 'Homokkő'),
    (100, 'Kovásodott andezitagglomerátum'),
    (110, 'Kvarcit'),
    (120, 'Lösz'),
    (121, 'Márga'),
    (122, 'Mészkő'),
    (130, 'Mésztufa'),
    (131, 'Perlit'),
    (140, 'Riolit'),
    (150, 'Riolittufa'),
    (160, 'Tráchit'),
    (170, 'Zöldpala'),
)

PROTECTION = (
    (10, 'Védett'),
    (20, 'Fokozottan védett'),
    (30, 'Megkülönböztetetten védett'),
)

ATTENDABILITY = (
    (10, 'Szabadon látogatható'),
    (20, 'Fokozottan védett területen nyíló'),
    (30, 'NPI hozzájárulásával látogatható (jogszabályban nevesített)'),
    (40, 'NPI hozzájárulásával látogatható (magánterületen nyíló)'),
    (50, 'Lezárt'),
    (60, 'Beomlott, jelenleg nem látogatható'),
)

NP = (
    (10, 'Aggteleki Nemzeti Park'),
    (20, 'Balaton-felvidéki Nemzeti Park'),
    (30, 'Bükki Nemzeti Park'),
    (40, 'Duna-Dráva Nemzeti Park'),
    (50, 'Duna-Ipoly Nemzeti Park'),
    (60, 'Fertő-Hanság Nemzeti Park'),
    (70, 'Hortobágyi Nemzeti Park'),
    (80, 'Kiskunsági Nemzeti Park'),
    (90, 'Kőrös-Maros Nemzeti Park'),
    (100, 'Őrségi Nemzeti Park'),
)


class Cave(BaseEntity):
    """ Barlang entitás """

    kataszteri_szam = models.CharField(
        verbose_name='Kataszteri szám',
        help_text='A magyarországi barlangkataszterben a barlang egyedi azonosítója',
        max_length=50)
    nev = models.CharField(verbose_name='Barlang neve', max_length=255)
    szinonimak = models.CharField(verbose_name='Barlang további elnevezései', max_length=255, null=True, blank=True)
    leiras = models.TextField(verbose_name='Leírás')
    kozet = models.IntegerField(verbose_name='Befoglaló kőzet', choices=SOUNDING_ROCK)
    vedettseg = models.IntegerField(verbose_name='Védettség', choices=PROTECTION)
    lathatosag = models.IntegerField(verbose_name='Látogathatóság', choices=ATTENDABILITY)
    illetekes_np = models.IntegerField(verbose_name='Illetékes NPI', choices=NP)
    eov_x = models.FloatField(verbose_name='EOV X')
    eov_y = models.FloatField(verbose_name='EOV Y')
    geom = gis_models.PointField(srid=4326)

    def __str__(self):
        return '{nev} ({kat_id})'.format(nev=self.nev, kat_id=self.kataszteri_szam)

    class Meta:
        ordering = ["nev"]
