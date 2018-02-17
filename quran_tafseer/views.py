# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.exceptions import NotFound

from .models import Tafseer, TafseerText
from .serializers import TafseerSerializer, TafseerTextSerializer


class TafseerView(generics.ListAPIView):
    serializer_class = TafseerSerializer
    queryset = Tafseer.objects.all().order_by('pk')


class AyahTafseerView(generics.RetrieveAPIView):
    serializer_class = TafseerTextSerializer
    model = TafseerText

    def get_object(self):
        tafseer_id = self.kwargs['tafseer_id']
        sura_index = self.kwargs['sura_index']
        ayah_number = self.kwargs['ayah_number']
        try:
            return TafseerText.objects.get_ayah_tafseer(tafseer_id,
                                                        sura_index,
                                                        ayah_number)
        except TafseerText.DoesNotExist:
            raise NotFound('Tafseer with provided id or '
                           'with sura and ayah ids not found')


class AyahTafseerRangeView(generics.ListAPIView):
    serializer_class = TafseerTextSerializer
    model = TafseerText

    def get_queryset(self):
        tafseer_id = self.kwargs['tafseer_id']
        sura_index = self.kwargs['sura_index']
        ayah_from = self.kwargs['ayah_from']
        ayah_to = self.kwargs['ayah_to']
        try:
            qs = TafseerText.objects.get_ayah_tafseer_range(tafseer_id,
                                                            sura_index,
                                                            ayah_from, ayah_to)
            return qs
        except TafseerText.DoesNotExist:
            raise NotFound('Tafseer with provided id, sura id, or range or '
                           'ayah are not found')
