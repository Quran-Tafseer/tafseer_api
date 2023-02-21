# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from core.views import MetricAPIGetMixin
from .models import Ayah, Sura
from .serializers import AyahSerializer, SuraSerializer

METRIC_DESC = "The number of request toward Quran Text. This includes getting Surahs, or Ayahat"


class SuraListView(generics.ListAPIView, MetricAPIGetMixin):
    """
    Returns a full list of quran's sura (chapters) sorted by the index
    """
    serializer_class = SuraSerializer
    queryset = Sura.objects.all()
    metric_desc = METRIC_DESC
    metric_name = "quran_req"


class AyahTextView(generics.RetrieveAPIView, MetricAPIGetMixin):
    """
    Returns Quran text for certain verse (Ayah) in a chapter (Sura)
    """
    serializer_class = AyahSerializer
    lookup_field = 'number'
    lookup_url_kwargs = 'number'
    metric_desc = METRIC_DESC
    metric_name = "quran_req"

    def get_queryset(self):
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.get_sura_text(sura_id)
        return qs
