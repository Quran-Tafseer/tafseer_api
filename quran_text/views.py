# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import SuraSerializer
from .models import Sura


class SuraListView(generics.ListAPIView):
    serializer_class = SuraSerializer
    queryset = Sura.objects.all()
