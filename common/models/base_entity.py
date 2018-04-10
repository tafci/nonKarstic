from django.contrib.auth.models import User
from django.db import models


class BaseEntity(models.Model):
    """ Entitások ősosztálya """

    created = models.DateTimeField(verbose_name='Létrehozás időpontja')
    creater = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_creaters")
    updated = models.DateTimeField(verbose_name='Utolsó módosítás időpontja', auto_now=True)
    updater = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_updaters")

    class Meta:
        abstract = True
