# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


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


class Ayah(models.Model):
    """
    Model to hold chapters' text ot Verse "Ayat"
    """
    number = models.PositiveIntegerField(verbose_name=_('Number'))
    sura = models.ForeignKey(Sura, related_name='ayat')
    text = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.sura.index, self.number)

    class Meta:
        unique_together = ['number', 'sura']
        ordering = ['sura', 'number']
