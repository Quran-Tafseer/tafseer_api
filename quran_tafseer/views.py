# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Tafseer, TafseerText
from .serializers import TafseerSerializer, TafseerTextSerializer


class TafseerView(generics.ListAPIView):
    serializer_class = TafseerSerializer
    queryset = Tafseer.objects.all()


class AyahTafseerView(generics.RetrieveAPIView):
    serializer_class = TafseerTextSerializer
    model = TafseerText

    def get_object(self):
        tafseer_id = self.kwargs['tafseer_id']
        sura_index = self.kwargs['sura_index']
        ayah_number = self.kwargs['ayah_number']
        return TafseerText.objects.get_ayah_tafseer(tafseer_id,
                                                    sura_index,
                                                    ayah_number)
