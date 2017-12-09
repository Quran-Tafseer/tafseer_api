# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sura(models.Model):
    """
    Model to hold the Quran Chapters "Sura"
    """
    index = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, verbose_name=_('Sura'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['index']


class AyahManager(models.Manager):

    def get_sura_text(self, sura_id):
        """Get all sura ayat"""
        return self.filter(sura_id=sura_id)

    def get_sura_ayah(self, sura_id, ayah_num):
        """Get one ayah from sura"""
        return self.get_sura_text(sura_id).filter(number=ayah_num)

    def get_sura_ayat_range(self, sura_id, from_ayah, to_ayah):
        """Get sura ayat from range (from ayah number to ahay number)"""
        return self.get_sura_text(sura_id).filter(number__lte=to_ayah,
                                                  number__gte=from_ayah)


class Ayah(models.Model):
    """
    Model to hold chapters' text ot Verse "Ayat"
    """
    number = models.PositiveIntegerField(verbose_name=_('Number'))
    sura = models.ForeignKey(Sura, related_name='ayat')
    text = models.TextField()
    objects = AyahManager()

    def __str__(self):
        return '{ayah.sura.index} - {ayah.number}'.format(ayah=self)

    class Meta:
        unique_together = ['number', 'sura']
        ordering = ['sura', 'number']
