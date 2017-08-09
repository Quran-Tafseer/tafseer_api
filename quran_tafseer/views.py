# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import TafseerSerializer
from .models import Tafseer


class TafseerView(generics.ListAPIView):
    serializer_class = TafseerSerializer
    queryset = Tafseer.objects.all()
