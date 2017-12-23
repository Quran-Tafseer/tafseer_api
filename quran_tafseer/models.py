# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from quran_text.models import Ayah


class Tafseer(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class TafseerTextManager(models.Manager):

    def get_sura_tafseer(self, tafseer_id, sura_id):
        return self.filter(ayah__sura_id=sura_id,
                           tafseer_id=tafseer_id)

    def get_ayah_tafseer(self, tafseer_id, sura_id, ayah_num):
        tafseer_text = self.get_sura_tafseer(tafseer_id, sura_id).filter(
            ayah__number=ayah_num
        ).first()
        if not tafseer_text:
            raise TafseerText.DoesNotExist
        return tafseer_text

    def get_ayah_tafseer_range(self, tafseer_id, sura_id, ayah_from_num, ayah_to_num):
        return self.get_sura_tafseer(tafseer_id, sura_id).filter(
            ayah__id__gte=ayah_from_num,
            ayah__id__lte=ayah_to_num
        )


class TafseerText(models.Model):
    tafseer = models.ForeignKey(Tafseer)
    ayah = models.ForeignKey(Ayah)
    text = models.TextField(verbose_name=_('Tafseer'))
    objects = TafseerTextManager()

    def __str__(self):
        return self.text
