# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from quran_text.models import Ayah


class Tafseer(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class TafseerText(models.Model):
    tafseer = models.ForeignKey(Tafseer)
    ayah = models.ForeignKey(Ayah)
    text = models.TextField(verbose_name=_('Tafseer'))

    def __str__(self):
        return self.text
