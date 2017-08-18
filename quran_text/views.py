# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import SuraSerializer, AyahSerializer
from .models import Sura, Ayah


class SuraListView(generics.ListAPIView):
    """
    Returns a full list of quran's sura (chapters) sorted by the index
    """
    serializer_class = SuraSerializer
    queryset = Sura.objects.all()


class AyahTextView(generics.RetrieveAPIView):
    """
    Returns Quran text for certain verse (Ayah) in a chapter (Sura)
    """
    serializer_class = AyahSerializer
    lookup_field = 'number'
    lookup_url_kwargs = 'number'

    def get_queryset(self):
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.get_sura_text(sura_id)
        return qs
