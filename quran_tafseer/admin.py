# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Tafseer, TafseerText


class TafseerAdmin(admin.ModelAdmin):
    pass


class TafseerTextAdmin(admin.ModelAdmin):
    list_display = ('tafseer', 'ayah', 'text')
    ordering = ['pk']


admin.site.register(Tafseer, TafseerAdmin)
admin.site.register(TafseerText, TafseerTextAdmin)
