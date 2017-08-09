# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import SuraSerializer, AyahSerializer
from .models import Sura, Ayah


class SuraListView(generics.ListAPIView):
    serializer_class = SuraSerializer
    queryset = Sura.objects.all()


class SuraAyatTextView(generics.ListAPIView):
    serializer_class = AyahSerializer
    lookup_field = 'sura_id'
    lookup_url_kwargs = 'sura_num'

    def get_queryset(self):
        # TODO return 404 if no ayat
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.get_sura_text(sura_id)
        return qs


class AyahRangeTextView(generics.ListAPIView):
    serializer_class = AyahSerializer

    def get_queryset(self):
        from_ayah = self.kwargs['ayah_from_num']
        to_ayah = self.kwargs['ayah_to_num']
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.get_sura_ayat_range(sura_id, from_ayah, to_ayah)
        return qs


class AyahTextView(generics.RetrieveAPIView):
    serializer_class = AyahSerializer
    lookup_field = 'number'
    lookup_url_kwargs = 'number'

    def get_queryset(self):
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.get_sura_text(sura_id)
        return qs
