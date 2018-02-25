# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework_tracking.mixins import LoggingMixin

from .models import Tafseer, TafseerText
from .serializers import TafseerSerializer, TafseerTextSerializer


class TafseerView(LoggingMixin, generics.ListAPIView):
    serializer_class = TafseerSerializer
    queryset = Tafseer.objects.all().order_by('pk')


class AyahTafseerView(LoggingMixin, generics.RetrieveAPIView):
    serializer_class = TafseerTextSerializer
    model = TafseerText
    next_ayah = None

    def get_object(self):
        tafseer_id = self.kwargs['tafseer_id']
        sura_index = self.kwargs['sura_index']
        ayah_number = self.kwargs['ayah_number']
        try:
            ayah_tafseer = TafseerText.objects.get_ayah_tafseer(tafseer_id,
                                                                sura_index,
                                                                ayah_number)
            next_ayah = ayah_tafseer.ayah.next_ayah()
            if next_ayah is not None:
                self.next_ayah = {'ayah_number': next_ayah.number,
                                  'sura_number': next_ayah.sura.index}
            return ayah_tafseer
        except TafseerText.DoesNotExist:
            raise NotFound('Tafseer with provided id or '
                           'with sura and ayah ids not found')

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args,
                                             **kwargs)
        if self.next_ayah:
            response['X-Next-Ayah'] = "{}:{}".format(
                self.next_ayah['sura_number'],
                self.next_ayah['ayah_number'])
        return response


class AyahTafseerRangeView(LoggingMixin, generics.ListAPIView):
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
